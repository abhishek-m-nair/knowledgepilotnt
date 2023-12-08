def get_system_prompt(language = 'English'):
    return f"""You are EVA. Assume the role of a professional physician/nurse talking to a patient 
        providing patient support. Your objective is to answer patient inquiries regarding their health and hospital stay. 
        Craft responses that offer comprehensive, scientifically-backed, and practical guidance while 
        considering the patient's personal details and medical history. 
        Make sure to address the patient by their name only once, as mentioned in the Patient History. 
        Additionally, infuse your responses with empathy and a caring tone, as if you were speaking to 
        the patient.  Be personal and warm. Talk as if you know the patient. 
        Don't use more than 50 words. Generate response in {language}. Do not add numbers to list\
        """

def get_patient_prompt(context, user_query):
    return f""""
        Patient Medical History: {context}
        Patient Query: {user_query}
        EVA Respone: Hello John, 
        """

#######doctor/nurse assistant prompts
def get_system_prompt_nurseassistant(language = 'English'):
    return f"""You are a physician/nurse assistant capable of assisting a physician/nurse during consultation for post discharge scenarios
        Given a scenario or query related to patient care or physician/nurse duties, provide a helpful and informative response. 
        Ensure that the reply is both accurate and compassionate, keeping in mind the best interests of the patient. 
        Additionally, make sure your response is generated in {language}.
        """

def get_patient_summary_prompt(history):
    return f"""
        Based on the patient medical history in json, generate a human readable summary for the physician.

        Create a structured summary with proper markups

        ### Patient Medical History:
        {history}
        ### Summary:
        """


###GTP 3.5-16k
def get_questions_prompt(patient_history, transcript):
    return f""""
        Based on the provided transcript snippets from a doctor-patient consultation, please parse the information 
        and generate potential questions the doctor could ask to facilitate the diagnosis process. 
        
        Please consider the patient's stated symptoms, their medical history, and any other relevant information presented in the transcript. 
        QUESTIONS SHOULD BE VERY SHORT. 
        Keep your response to not more than 100 words and give only 2 questions
        1. how are you managing type 2 diabetes
        2. describe your recovery process

        Create a structured response with proper markups

        Patient history:
        {patient_history}

        Transcript:
        {transcript}

        Potential Questions:
        Based on the provided patient history, here are three potential questions the doctor could ask to facilitate the diagnosis process:
        """
###GPT-4
def get_progress_note_prompt(patient_history, transcript):
    return f"""
        Based on the patient medical history, conversation transcript and doctor's diagnosis
        provided below, generate a progress clinical note in the following format:
        Diagnosis:
        History of Presenting Illness:
        Medications (Prescribed): List current medications and note if they are being continued, or if any new ones have been added.
        Lab Tests (Ordered):
        Create a structured response with proper markups.

        ### Patient Medical History:
        {patient_history}
        ### Conversation Transcript:
        {transcript}
        ### Clinical Note:
        """


###GPT-4
def get_soap_note_prompt(patient_history, transcript):
    return f"""
        Based on the patient medical history, conversation transcript and doctor's diagnosis
        provided below, generate a very detailed soap note

        Now, based on the following conversation and hints, please generate a very short SOAP clinical note. 

        Create a structured response with proper markups. Create section headers in bold. Every section should be a seperate block. The generation should look professional

        ### Patient Medical History:
        {patient_history}
        ### Conversation Transcript:
        {transcript}
        ### SOAP Note:
        """


# ###GTP 3.5-16k
# def get_diagnosis_questions_prompt(patient_history, transcript):
#     return f""""
#         Based on the provided transcript snippets from a doctor-patient consultation, please parse the information and generate a differential diagnosis, as well as potential questions the doctor could ask to facilitate the diagnosis process. The results should be organized in the following format:
#         Differential Diagnosis: List each possible diagnosis (not more than 5) with a model confidence score from 0-100, 100 being most confident.
#         Questions to Ask: Provide a list of not more than 3 relevant questions the doctor could ask to further clarify the diagnosis.
#         Please consider the patient's stated symptoms, their medical history, and any other relevant information presented in the transcript. 
#         DONOT GIVE ANY DISCLAIMER. THE RECIPIENT IS ALREADY AWARE OF THE RISK
#         The consultation snippets are as follows:
#         Patient history:
#         {patient_history}
#         Transcript:
#         {transcript}
#         """
# ###GTP 3.5-16k
# def get_diagnosis_prompt(patient_history, transcript):
#     return f""""
#         Based on the provided transcript snippets from a doctor-patient consultation, please parse the information 
#         and generate a differential diagnosis. The results should be as following:
#         Differential Diagnosis: List each possible diagnosis (not more than 3) with a model confidence score from 0-100, 100 being most confident.
        
#         Please consider the patient's stated symptoms, their medical history, and any other relevant information presented in the transcript. 
#         DONOT GIVE ANY DISCLAIMER. THE RECIPIENT IS ALREADY AWARE OF THE RISK
#         The consultation snippets are as follows:
#         Patient history:
#         {patient_history}
#         Transcript:
#         {transcript}
#         """

# ###GPT-4
# def get_progress_note_prompt(patient_history, transcript):
#     return f"""
#         Based on the patient medical history, conversation transcript and doctor's diagnosis
#         provided below, generate a clinical note in the following format:
#         Diagnosis:
#         History of Presenting Illness:
#         Medications (Prescribed): List current medications and note if they are being continued, or if any new ones have been added.
#         Lab Tests (Ordered):
#         Please consider any information in the transcript that might be relevant to each of these sections, and use the doctor's diagnosis as a guide.

#         ### Example

#         ### Conversation Transcript:
#         Patient: “I've been taking the Glycomet-GP 1 as you prescribed, doctor, but I'm still feeling quite unwell. My blood pressure readings are all over the place and my sugar levels are high.”
#         Doctor: “I see, we may need to adjust your medications. Let's add Jalra-OD and Telmis to your regimen and see how you respond.”
        
#         ###Clinical Note:
#         Diagnosis: Uncontrolled Diabetes and Hypertension
#         History of Presenting Illness: The patient has been adhering to their current medication regimen but the diabetes and hypertension seem uncontrolled.
#         Medications (Prescribed):
#         [Continue] Glycomet-GP 1 (tablet) | Glimepiride and Metformin
#         [Added] Jalra-OD 100mg (tablet) | Vildagliptin
#         [Added] Telmis 20 (Tablet)
#         Lab Tests (Ordered): None
    
#         Now, based on the following conversation and hints, please generate a clinical note:

#         ### Patient Medical History:
#         {patient_history}
#         ### Conversation Transcript:
#         {transcript}
#         ### Clinical Note:
#         """