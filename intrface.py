import streamlit as st
import joblib as jb
from streamlit_option_menu import option_menu

RF=jb.load(open('C:/Users/Admin/Desktop/SEM 5 project/clfRF_model.pkl','rb'))

with st.sidebar:
    selected=option_menu("Disease Prediction and Specilist Selection",
                         ['Disease Prediction',
                          'Consult Specialist'],
                         icons=['clipboard2-pulse-fill','heart-pulse-fill'],
                         default_index=0
    )

Symptom1=None
Symptom2=None
Symptom3=None
Symptom4=None
Symptom5=None
Symptom6=None


if(selected=='Disease Prediction'):
    st.title('Disease Prediction Uising Random Forest in ML')
    
    options = {

    "Abdominal pain": "abdominal_pain",
    "Abnormal menstruation":"abnormal_menstruation",
    "acidity"	:	    "acidity"	,
    "acute liver failure"	:	    "acute_liver_failure"	,
    "altered sensorium"	:	    "altered_sensorium"	,
    "anxiety"	:	    "anxiety"	,
    "back pain"	:	    "back_pain"	,
    "belly pain"	:	    "belly_pain"	,
    "blackheads"	:	    "blackheads"	,
    "bladder discomfort"	:	    "bladder_discomfort"	,
    "blister"	:	    "blister"	,
    "blood in sputum"	:	    "blood_in_sputum"	,
    "bloody stool"	:	    "bloody_stool"	,
    "blurred and distorted vision"	:	    "blurred_and_distorted_vision"	,
    "breathlessness"	:	    "breathlessness"	,
    "brittle nails"	:	    "brittle_nails"	,
    "bruising"	:	    "bruising"	,
    "burning micturition"	:	    "burning_micturition"	,
    "chest pain"	:	    "chest_pain"	,
    "chills"	:	    "chills"	,
    "cold hands and feets"	:	    "cold_hands_and_feets"	,
    "coma"	:	    "coma"	,
    "congestion"	:	    "congestion"	,
    "constipation"	:	    "constipation"	,
    "continuous feel of urine"	:	    "continuous_feel_of_urine"	,
    "continuous sneezing"	:	    "continuous_sneezing"	,
    "cough"	:	    "cough"	,
    "cramps"	:	    "cramps"	,
    "dark urine"	:	    "dark_urine"	,
    "dehydration"	:	    "dehydration"	,
    "depression"	:	    "depression"	,
    "diarrhoea"	:	    "diarrhoea"	,
    "dischromic patches"	:	    "dischromic _patches"	,
    "distention of abdomen"	:	    "distention_of_abdomen"	,
    "dizziness"	:	    "dizziness"	,
    "drying and tingling lips"	:	    "drying_and_tingling_lips"	,
    "enlarged thyroid"	:	    "enlarged_thyroid"	,
    "excessive hunger"	:	    "excessive_hunger"	,
    "extra marital contacts"	:	    "extra_marital_contacts"	,
    "family history"	:	    "family_history"	,
    "fast heart rate"	:	    "fast_heart_rate"	,
    "fatigue"	:	    "fatigue"	,
    "fluid overload"	:	    "fluid_overload"	,
    "foul smell of urine"	:	    "foul_smell_of urine"	,
    "headache"	:	    "headache"	,
    "high fever"	:	    "high_fever"	,
    "hip joint pain"	:	    "hip_joint_pain"	,
    "history of alcohol consumption"	:	    "history_of_alcohol_consumption"	,
    "increased appetite"	:	    "increased_appetite"	,
    "indigestion"	:	    "indigestion"	,
    "inflammatory nails"	:	    "inflammatory_nails"	,
    "internal itching"	:	    "internal_itching"	,
    "irregular sugar level"	:	    "irregular_sugar_level"	,
    "irritability"	:	    "irritability"	,
    "irritation in anus"	:	    "irritation_in_anus"	,
    "itching"	:	    "itching"	,
    "joint pain"	:	    "joint_pain"	,
    "knee pain"	:	    "knee_pain"	,
    "lack of concentration"	:	    "lack_of_concentration"	,
    "lethargy"	:	    "lethargy"	,
    "loss of appetite"	:	    "loss_of_appetite"	,
    "loss of balance"	:	    "loss_of_balance"	,
    "loss of smell"	:	    "loss_of_smell"	,
    "malaise"	:	    "malaise"	,
    "mild fever"	:	    "mild_fever"	,
    "mood swings"	:	    "mood_swings"	,
    "movement stiffness"	:	    "movement_stiffness"	,
    "mucoid sputum"	:	    "mucoid_sputum"	,
    "muscle pain"	:	    "muscle_pain"	,
    "muscle wasting"	:	    "muscle_wasting"	,
    "muscle weakness"	:	    "muscle_weakness"	,
    "nausea"	:	    "nausea"	,
    "neck pain"	:	    "neck_pain"	,
    "nodal skin eruptions"	:	    "nodal_skin_eruptions"	,
    "obesity"	:	    "obesity"	,
    "pain behind the eyes"	:	    "pain_behind_the_eyes"	,
    "pain during bowel movements"	:	    "pain_during_bowel_movements"	,
    "pain in anal region"	:	    "pain_in_anal_region"	,
    "painful walking"	:	    "painful_walking"	,
    "palpitations"	:	    "palpitations"	,
    "passage of gases"	:	    "passage_of_gases"	,
    "patches in throat"	:	    "patches_in_throat"	,
    "phlegm"	:	    "phlegm"	,
    "polyuria"	:	    "polyuria"	,
    "prognosis"	:	    "prognosis"	,
    "prominent veins on calf"	:	    "prominent_veins_on_calf"	,
    "puffy face and eyes"	:	    "puffy_face_and_eyes"	,
    "pus filled pimples"	:	    "pus_filled_pimples"	,
    "receiving blood transfusion"	:	    "receiving_blood_transfusion"	,
    "receiving unsterile injections"	:	    "receiving_unsterile_injections"	,
    "red sore around nose"	:	    "red_sore_around_nose"	,
    "red spots over body"	:	    "red_spots_over_body"	,
    "redness of eyes"	:	    "redness_of_eyes"	,
    "restlessness"	:	    "restlessness"	,
    "runny nose"	:	    "runny_nose"	,
    "rusty sputum"	:	    "rusty_sputum"	,
    "scurring"	:	    "scurring"	,
    "shivering"	:	    "shivering"	,
    "silver like dusting"	:	    "silver_like_dusting"	,
    "sinus pressure"	:	    "sinus_pressure"	,
    "skin peeling"	:	    "skin_peeling"	,
    "skin rash"	:	    "skin_rash"	,
    "slurred speech"	:	    "slurred_speech"	,
    "small dents in nails"	:	    "small_dents_in_nails"	,
    "spinning movements"	:	    "spinning_movements"	,
    "spotting urination"	:	    "spotting_ urination"	,
    "stiff neck"	:	    "stiff_neck"	,
    "stomach bleeding"	:	    "stomach_bleeding"	,
    "stomach pain"	:	    "stomach_pain"	,
    "sunken eyes"	:	    "sunken_eyes"	,
    "sweating"	:	    "sweating"	,
    "swelled lymph nodes"	:	    "swelled_lymph_nodes"	,
    "swelling joints"	:	    "swelling_joints"	,
    "swelling of stomach"	:	    "swelling_of_stomach"	,
    "swollen blood vessels"	:	    "swollen_blood_vessels"	,
    "swollen extremeties"	:	    "swollen_extremeties"	,
    "swollen legs"	:	    "swollen_legs"	,
    "throat irritation"	:	    "throat_irritation"	,
    "toxic look (typhos)"	:	    "toxic_look_(typhos)"	,
    "ulcers on tongue"	:	    "ulcers_on_tongue"	,
    "unsteadiness"	:	    "unsteadiness"	,
    "visual disturbances"	:	    "visual_disturbances"	,
    "vomiting"	:	    "vomiting"	,
    "watering from eyes"	:	    "watering_from_eyes"	,
    "weakness in limbs"	:	    "weakness_in_limbs"	,
    "weakness of one body side"	:	    "weakness_of_one_body_side"	,
    "weight gain"	:	    "weight_gain"	,
    "weight loss"	:	    "weight_loss"	,
    "yellow crust ooze"	:	    "yellow_crust_ooze"	,
    "yellow urine"	:	    "yellow_urine"	,
    "yellowing of eyes"	:	    "yellowing_of_eyes"	,
    "yellowish skin"	:	    "yellowish_skin"	,
	}
    

selected_option = st.selectbox("Select an option:", list(options.keys()))

if st.button('Predicted Disease'):
    Symptom1=selected_option
st.write('you select',Symptom1)
if(selected=='Consult Specialist'):
    st.title('Dr. specialization Prediction Uising Random Forest in ML')
    
    