import openai as openaimain
import os
import json
from gptcache import cache
from gptcache.adapter import openai as cacheopenai
from gptcache.embedding.openai import OpenAI
from gptcache.manager import CacheBase, VectorBase, get_data_manager
# from gptcache.similarity_evaluation.distance import SearchDistanceEvaluation
# from gptcache.similarity_evaluation.sbert_crossencoder import SbertCrossencoderEvaluation
from gptcache.similarity_evaluation.np import NumpyNormEvaluation
from gptcache.config import Config
from postadmission_genai_pack.logger import get_logger
logger = get_logger(__name__)

from dotenv import load_dotenv
# Load environmental variables
load_dotenv()

OPENAI_TOKEN = os.getenv("OPENAI_API_KEY")
openaimain.api_key = OPENAI_TOKEN

model = os.getenv("MODEL", "gpt-3.5-turbo")
logger.info(f'using model {model}')

cache_threshold = os.getenv("CACHE_THRESHOLD", 0.85)

print("Cache loading.....")

# onnx = Onnx()
openai = OpenAI(api_key=OPENAI_TOKEN)
data_manager = get_data_manager(CacheBase("sqlite"), VectorBase("faiss", dimension=openai.dimension))

config = Config(similarity_threshold=float(cache_threshold))

cache.init(
    embedding_func=openai.to_embeddings,
    data_manager=data_manager,
    # similarity_evaluation=SearchDistanceEvaluation(),
    # similarity_evaluation=SbertCrossencoderEvaluation()
    similarity_evaluation= NumpyNormEvaluation(),
    config=config
    )

cache.set_openai_key()

# from gptcache import cache
# from gptcache.adapter import openai as cacheopenai

# cache.init()
# cache.set_openai_key()

##method for exact completion cache
def get_completion_cache(sys_prompt, prompt, history = None, temperature = 1):
    messages = []
    messages.append({"role": "system", "content": sys_prompt})
    
    logger.info(f'temperature: {temperature}')
    if history:  # Only append history if there is some
        messages.extend(history)
    
    messages.append({"role": "user", "content": prompt})
    logger.debug(f'messages: {messages}')
    response = cacheopenai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response_text(response)

def get_completion(sys_prompt, prompt, history = None):
    messages = []
    messages.append({"role": "system", "content": sys_prompt})
    
    if history:  # Only append history if there is some
        messages.extend(history)
    
    messages.append({"role": "user", "content": prompt})
    logger.debug(f'messages: {messages}')
    response = openaimain.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response_text(response)


def get_completion_batch(sys_prompt, prompt_lst, history = None):
    messages = []
    messages.append({"role": "system", "content": sys_prompt})
    
    if history:  # Only append history if there is some
        messages.extend(history)
    
    stringifiedPromptsArray = json.dumps(prompt_lst)

    messages.append({"role": "user", "content": stringifiedPromptsArray})
    logger.debug(f'messages: {messages}')
    response = openaimain.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response_text_batch(response)


    # return response.choices[0].message["content"]

def get_completion_stream(sys_prompt, prompt, history = None):
    messages = []
    messages.append({"role": "system", "content": sys_prompt})
    
    if history:  # Only append history if there is some
        messages.extend(history)
    
    messages.append({"role": "user", "content": prompt})
    logger.debug(f'messages: {messages}')
    completion = openaimain.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
        stream=True
    )

    for chunk in completion:
        delta = chunk['choices'][0]['delta']
        if 'content' in delta.keys():
            yield delta['content']

def response_text(openai_resp):
    return openai_resp['choices'][0]['message']['content']

def response_text_batch(openai_resp):
    responses = []
    for choice in openai_resp.choices:
        responses.append(choice['message']['content'])

    return responses