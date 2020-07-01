MondayAM = {"AMPM":"AM",
    "DAY":"MONDAY",
    "JDB0B":["DB","REG",(1,2,3,4,5),"KEEP"],
    "JSL0A":["SL","CONS",(1,2,3,4,5), "DROP"],
    "JSL0B":["SL","REG",(1,2,3,4,5),"KEEP"],
    "JSSALLERGY":["SS","CONS",(1,),"KEEP"],
    "SJJA0":["SS", "CONS", (2,4),"KEEP"],
    "JDB0A":["DB","CONS",(2,3,5),"KEEP"],
    "JDBCONSREF":["DB","CONS",(4,),"KEEP"],
    "2015":["NT","NUR",(1,2,3,4,5),"KEEP"],
    "CAS":["JD","JD",(1,2,3,4,5),"KEEP"],

    }

#    "test":["SL","StG1",(1,2,3,4,5)]

MondayPM = {
    "AMPM":"PM",
    "DAY":"MONDAY",
    "JSL2W1AA":["SL","CONS",(3,),"KEEP"],
    "JSL2W1B":["SL", "REG", (1,2,3,4,5),"KEEP"],
    "JSL2W1A":["SL", "CONS",(2,4),"KEEP"],
    "JDBCLEFT":["DB", "CONS", (1,2,3,4,5),"KEEP"],
    "JSS1A":["DB", "CONS",(1,2,3,4,5),"KEEP"],
    "JRW2W1AA":["RGW","CONS",(1,2,4,5),"KEEP"],
    "2015":["NT","NUR",(1,2,3,4,5),"KEEP"],
    "CAS":["JD","JD",(1,2,3,4,5),"KEEP"],
    "JKB4A":["KB","CONS",(1,2,4,5),"MOVE"],
    }

TuesdayAM = {"AMPM":"AM",
    "DAY":"TUESDAY",
    "JDL2A":["DL","CONS",(1,2,3,4,5),"DROP"],
    "JDL2B":["DL","REG",(1,2,3,4,5),"KEEP"],
    "JDB2A":["DB","CONS",(1,3,4,5),"KEEP"],
    "JDB2T":["DB","CONS",(2,),"KEEP"],
    "JSB2N":["NT", "NUR", (1,2,3,4,5),"KEEP"],
    "JNA2A":["NA","CONS",(2,),"KEEP"],
    "JSS2A":["SS","CONS",(1,2,3,4,5),"KEEP"],
    "2015":["NT","NUR",(1,2,3,4,5),"KEEP"],
    "CAS":["JD","JD",(1,2,3,4,5),"KEEP"]
    }

TuesdayPM = {
    "AMPM":"PM",
    "DAY":"TUESDAY",
    "JDL3B":["DL","REG",(1,3,4,5),"KEEP"],
    "JSS3A":["SS", "CONS", (1,2,3,4,5),"KEEP"],
    "JNACOCHLEA":["NA", "CONS",(2,4),"KEEP"],
    "JNA3A":["NA", "CONS", (1,3,5),"KEEP"],
    "JDL3A1":["DL", "CONS",(3,4),"KEEP"],
    "2987/2695":["DL","CONS",(1,),"KEEP"],
    "JAB3A":["AB","CONS",(1,2,3,4,5),"KEEP"],
    "JAB3B":["AB","REG",(1,2,3,4,5),"KEEP"],
    "2015":["NT","NUR",(1,2,3,4,5),"KEEP"],
    "CAS":["JD","JD",(1,2,3,4,5),"KEEP"]
    }

WednesdayAM = {"AMPM":"AM",
    "DAY":"WEDNESDAY",
    "JKB4A":["KB","CONS",(1,2,4,5),"DROP"],
    "JKBPVT":["KB","CONS",(3,),"DROP"],
    "JDB4B":["KB","REG",(1,2,3,4,5),"KEEP"],
    "JKB4C":["GT","CONS",(1,3,),"KEEP"],
    "JABCOCHLEA":["AB","CONS",(2,),"KEEP"],
    "2015N":["NT","NUR",(3,5),"KEEP"],
    "2015":["NT","NUR",(1,2,3,4,5),"KEEP"],
    "CAS":["JD","JD",(1,2,3,4,5),"KEEP"],
    "JNABOTOX":["NA", "CONS", (3,),"SPECIALIN"],
    }

#    "JRW2W4C":["RGW", "StG", (1,2,3,4,5)],

WednesdayPM = {
    "AMPM":"PM",
    "DAY":"WEDNESDAY",
    "JNABOTNEW":["NA","CONS",(1,),"KEEP"],
    "JNABOTOX":["NA", "CONS", (2,4,5),"KEEP"],
    "JNABOTOX":["NA", "CONS", (3,),"SPECIALOUT"],
    "JNA5B":["NA", "CONS",(1,2,3,4,5),"KEEP"],
    "JKB5A1":["KB", "CONS", (1,),"KEEP"],
    "JKB5A":["KB", "CONS",(2,3,4,5),"KEEP"],
    "JKB5B":["KB","REG",(1,2,3,4,5),"KEEP"],
    "JDW5A":["DW","CONS",(2,3,4,5),"KEEP"],
    "2015AC":["NT","NUR",(5,),"KEEP"],
    "2015":["NT","NUR",(1,2,3,4),"KEEP"],
    "JSB4E EVENING":["SB","NT",(1,2,3,4,5),"KEEP"],
    "2015/2015AC EVENING":["SB","NUR",(1,2,3,4,5),"KEEP"],
    "CAS":["JD","JD",(1,2,3,4,5),"KEEP"],
    "JKBPVT":["KB","CONS",(3,),"MOVE"],
    }

ThursdayAM = {"AMPM":"AM",
    "DAY":"THURSDAY",
    "1088AA_main":["HAN","CONS",(1,2,3,4,5),"KEEP"],
    "1088AA_small":["HAN","CONS",(1,2,3,4,5),"KEEP"],
    "JRS2W6A + 1088EE":["RS","CONS",(1,2,3,4,5),"KEEP"],
    "1088D":["HAN3","CONS",(1,2,3,4,5),"KEEP"],
    "DIETICIAN":["AHP","AHP",(1,2,3,4,5),"KEEP"],
    "TRACHE":["SL", "NUR", (1,2,3,4,5),"KEEP"],
    "CAS":["JD","JD",(1,2,3,4,5),"KEEP"]
    }

ThursdayPM = {
    "AMPM":"PM",
    "DAY":"THURSDAY",
    "2695":["DL","CONS",(1,3),"KEEP"],
    "1088C":["SL", "StG", (2,4,5),"KEEP"],
    "JDW7A":["DW", "CONS", (1,2,3,4,5),"KEEP"],
    "741":["CC", "NUR",(1,2,3,4,5),"KEEP"],
    "2015AC":["NT","NUR",(1,2,3,4,5),"KEEP"],
    "2015 EVENING *2":["SB","NUR",(1,2,3,4,5),"KEEP"],
    "CAS":["JD","JD",(1,2,3,4,5),"KEEP"]
    }


FridayAM = {"AMPM":"AM",
    "DAY":"FRIDAY",
    "JAB8A":["AB","CONS",(1,2,3,4,5),"DROP"],
    "JAB8C":["GT","CONS",(1,2,3,4,5),"KEEP"],
    "2695":["DL","CONS",(2,5),"DROP"],
    "JSL2W8A/JSLVCORD":["SL","CONS",(1,2,3,4,5),"DROP"],
    "797":["CC", "NUR", (1,2,3,4,5),"KEEP"],
    "2015":["NT","NUR",(1,2,3,4,5),"KEEP"],
    "CAS":["JD","JD",(1,2,3,4,5),"KEEP"],
    }

FridayPM = {
    "AMPM":"PM",
    "DAY":"FRIDAY",
    "JSS9A":["SS","CONS",(1,3,5),"KEEP"],
    "JDL9A/2987":["DL", "CONS", (2,5),"KEEP"],
    "JSH9A":["SH", "CONS",(2,4,),"KEEP"],
    "797":["CC", "NUR", (1,2,3,4,5),"KEEP"],
    "JRW2W9A":["RGW", "CONS", (1,2,3,4,5),"KEEP"],

    "SALT VOICE":["MS","AHP",(3,),"KEEP"],
    "CAS":["JD","JD",(1,2,3,4,5),"KEEP"]
    }

#    "JSL2W9C":["SL", "StG",(1,2)],
#    "JDL9C":["DL","StG",(3,4,5)],

days = [MondayAM, MondayPM, TuesdayAM, TuesdayPM, WednesdayAM, WednesdayPM, ThursdayAM, ThursdayPM, FridayAM, FridayPM]

#staff grade must include consultants you work for
Registrars =[
    "Nil",
    "SL_RGW_SH_REG",
    "NA_AB_REG",
    "DW_DL_REG",
    "KB_DB_REG",
    "Locum",
    "MK_StG1",
    "ME_StG2"
    ]

Consultants = [
    "SL",
    "SH",
    "NA",
    "GT",
    "AB",
    "DL",
    "DW",
    "KB",
    "RGW",
    "SS",
    "RS",
    ]

weekdays = [
    "1  Mon",
    "2  Tue",
    "3  Wed",
    "4  Thur",
    "5  Fri"
    ]