def dict_label(key, reverse=False):
    maritalDict = {
        "1" : "Single", 
        "2" : "Married", 
        "3" : "Widower", 
        "4" : "Divorced", 
        "5" : "Facto Union",
        "6" : "Legally Separated"
    }

    courseDict = {
        "33" : "Biofuel Production Technologies",
        "171" : "Animation and Multimedia Design ",
        "8014" : "Social Service (evening attendance)", 
        "9003" : "Agronomy",
        "9070" : "Communication Design", 
        "9085" : "Veterinary Nursing",
        "9119" : "Informatics Engineering", 
        "9130" : "Equinculture",
        "9147" : "Management",
        "9238" : "Social Service", 
        "9254" : "Tourism",
        "9500" : "Nursing", 
        "9556" : "Oral Hygiene", 
        "9670" : "Advertising and Marketing Management", 
        "9773" : "Journalism and Communication", 
        "9853" : "Basic Education", 
        "9991" : "Management (evening attendance)",
    }

    prevQualificationDict = {
        "1"  : "Secondary education", 
        "2"  : "Higher education : bachelor's degree", 
        "3"  : "Higher education : degree", 
        "4"  : "Higher education : master's", 
        "5"  : "Higher education : doctorate",
        "6"  : "Frequency of higher education", 
        "9"  : "12th year of schooling : not completed", 
        "10" : "11th year of schooling : not completed",
        "12" : "Other : 11th year of schooling", 
        "14" : "10th year of schooling", 
        "15" : "10th year of schooling : not completed", 
        "19" : "Basic education 3rd cycle (9th/10th/11th year) or equiv.", 
        "38" : "Basic education 2nd cycle (6th/7th/8th year) or equiv.", 
        "39" : "Technological specialization course", 
        "40" : "Higher education : degree (1st cycle)", 
        "42" : "Professional higher technical course",
        "43" : "Higher education : master (2nd cycle)",
    }

    Nacionality = {
        "1" : "Portuguese", 
        "2" : "German", 
        "6" : "Spanish", 
        "11" : "Italian", 
        "13" : "Dutch", 
        "14" : "English", 
        "17" : "Lithuanian", 
        "21" : "Angolan", 
        "22" : "Cape Verdean", 
        "24" : "Guinean", 
        "25" : "Mozambican", 
        "26" : "Santomean", 
        "32" : "Turkish", 
        "41" : "Brazilian", 
        "62" : "Romanian", 
        "100" : "Moldova (Republic of)", 
        "101" : "Mexican", 
        "103" : "Ukrainian", 
        "105" : "Russian", 
        "108" : "Cuban", 
        "109" : "Colombian"
    }

    job = {
        "0"   : "Student",
        "1"   : "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers", 
        "2"   : "Specialists in Intellectual and Scientific Activities", 
        "3"   : "Intermediate Level Technicians and Professions", 
        "4"   : "Administrative staff", 
        "5"   : "Personal Services, Security and Safety Workers and Sellers", 
        "6"   : "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry", 
        "7"   : "Skilled Workers in Industry, Construction and Craftsmen", 
        "8"   : "Installation and Machine Operators and Assembly Workers", 
        "9"   : "Unskilled Workers",
        "10"  : "Armed Forces Professions",
        "90"  : "Other Situation",
        "99"  : "",
        "101" : "Armed Forces Officers", 
        "102" : "Armed Forces Sergeants",
        "103" : "Other Armed Forces personnel", 
        "112" : "Directors of administrative and commercial services", 
        "114" : "Hotel, catering, trade and other services directors",
        "121" : "Specialists in the physical sciences, mathematics, engineering and related techniques",
        "122" : "Health professionals", 
        "123" : "teachers",
        "124" : "Specialists in finance, accounting, administrative organization, public and commercial relations",
        "125" : "Specialists in information and communication technologies (IT)", 
        "131" : "Intermediate level science and engineering technicians and professions", 
        "132" : "Technicians and professionals, of intermediate level of health", 
        "134" : "Intermediate level technicians from legal, social, sports, cultural and similar services",
        "135" : "Information and communication technology technicians",
        "141" : "Office workers, secretaries in general and data processing operators", 
        "143" : "Data, accounting, statistical, financial services and registry-related operators",
        "144" : "Other administrative support staff",
        "151" : "personal service workers", 
        "152" : "sellers",
        "154" : "Protection and security services personnel",
        "161" : "Market-oriented farmers and skilled agricultural and animal production workers", 
        "163" : "Farmers, livestock keepers, fishermen, hunters and gatherers, subsistence",
        "153" : "Personal care workers and the like", 
        "171" : "Skilled construction workers and the like, except electricians",
        "172" : "Skilled workers in metallurgy, metalworking and similar",
        "173" : "Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like",
        "174" : "Skilled workers in electricity and electronics",
        "181" : "Fixed plant and machine operators",
        "182" : "assembly workers",
        "183" : "Vehicle drivers and mobile equipment operators",
        "175" : "Workers in food processing, woodworking, clothing and other industries and crafts",
        "191" : "cleaning workers", 
        "192" : "Unskilled workers in agriculture, animal production, fisheries and forestry", 
        "193" : "Unskilled workers in extractive industry, construction, manufacturing and transport",
        "194" : "Meal preparation assistants",
        "195" : "Street vendors (except food) and street service providers"
    }

    attendaceDict = {"1" : "Daytime", "0" : "Evening"}
    maleFemaleDict = {"1" : "Male", "0" : "Female"}
    yesNoDict = {"1" : "Yes", "0" : "No"}
    
    dictClass = {
        "Marital_status" : maritalDict,
        "Course" : courseDict,
        "Previous_qualification" : prevQualificationDict,
        "Nacionality" : Nacionality,
        "occupation" : job,
        "Daytime_evening_attendance" : attendaceDict,
        "Gender" : maleFemaleDict,
        "yes_no" : yesNoDict
    }
    
    if reverse :
        return {value: key for key, value in dictClass[key].items()}
    else :
        return dictClass[key]