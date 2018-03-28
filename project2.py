#import dependencies
import requests
import pandas as pd
import json
import pprint as pp

    

#Get PandaScore
#series_old = "https://api.pandascore.co/series?token="

#Need to store teamIDs, Description

leagues = "https://api.pandascore.co/videogames/1/leagues?year=2018&token="
    #ID's for consideration -
        #EU LCS id: 290
        #NA LCS id: 289
        #LCK id: 293
        #LPL id: 294
        #LMS id: 295
series = "https://api.pandascore.co/videogames/1/series?year=2018&token="
seriesmatches = "https://api.pandascore.co/videogames/1/series/1343/matches?year=2018&token="
tournaments= "https://api.pandascore.co/videogames/1/tournaments?token="
teams= "https://api.pandascore.co/videogames/1/teams?token="
videogames = "https://api.pandascore.co/videogames/1?token="
EULCSmatches = "https://api.pandascore.co/tournaments/684/matches?token="
NALCSmatches = "https://api.pandascore.co/tournaments/652/matches?token="

pages = "?page=X+1>; rel="next""




api_key = "SJnR-aaQcMjV_OGI4Ip_MOqYDH-ZwLLHdhda1cRyAHPTpCpz9a8"

response = requests.get(leagues+api_key)
league_id = response.json()
pydata = json.dumps(league_id)
pydata = pd.read_json(pydata)
league_id = pydata[['id','name']]
values=[289,290]
NAEULCSLeague_id = league_id.loc[league_id['id'].isin(values)]
print('League_ID')
pp.pprint(NAEULCSLeague_id)
print('')
print('=========================================')
print('')

#Get Series ID for NALCS and EULCS Spring
    #EULCS serie_id = 1343
    #NALCS serie_id = 1333
series = requests.get(series+api_key)
series = series.json()
series = json.dumps(series)
series = pd.read_json(series)
series_id = series[['id','name','season','league_id','year']]

print('Series_ID')
pp.pprint(series_id)
print('')
print('========================================')
print('')

#Get Match IDs for EULCS
#Get Win Count By Team
#Get List of Teams

EULCSteams = []
G2_win = 0
SPY_win = 0
VIT_win = 0
UOL_win = 0
FNC_win = 0
ROC_win = 0
S04_win = 0
MSF_win = 0
GIA_win = 0
H2K_win = 0
counter = 0

EULCSmatches = requests.get(EULCSmatches+api_key + page)
EULCSmatches = EULCSmatches.json()
#Tournament id for spring split = 684
matchid = EULCSmatches[0]['id']
name = EULCSmatches[0]['name']
winner = EULCSmatches[0]['winner']['name']

for 0 < i < 3 in page
    for i in range(len(EULCSmatches)):

        try:
            # print('')
            #print(EULCSmatches[i]['id'])
            #print(EULCSmatches[i]['name'])
            #print(EULCSmatches[i]['winner']['name'])
            if EULCSmatches[i]['winner']['name'] not in EULCSteams:
                EULCSteams.append(EULCSmatches[i]['winner']['name'])
            # print('')

            if EULCSmatches[i]['tournament_id'] == 684 and EULCSmatches[i]['winner']['name'] == 'G2 Esports':
                G2_win = G2_win + 1
                #print("G2_wins :" + str(G2_win))
            elif EULCSmatches[i]['tournament_id'] == 684 and EULCSmatches[i]['winner']['name'] == 'Splyce':
                SPY_win = SPY_win + 1
                #print("SPY_wins :" + str(SPY_win))
            elif EULCSmatches[i]['tournament_id'] == 684 and EULCSmatches[i]['winner']['name'] == 'Unicorns Of Love':
                UOL_win = UOL_win + 1
                #print("UOL_wins :" + str(UOL_win))
            elif EULCSmatches[i]['tournament_id'] == 684 and EULCSmatches[i]['winner']['name'] == 'Vitality':
                VIT_win = VIT_win + 1
                #print("VIT_wins :" + str(VIT_win))
            elif EULCSmatches[i]['tournament_id'] == 684 and EULCSmatches[i]['winner']['name'] == 'Fnatic':
                FNC_win = FNC_win + 1
                #print("FNC_wins :" + str(FNC_win))
            elif EULCSmatches[i]['tournament_id'] == 684 and EULCSmatches[i]['winner']['name'] == 'ROCCAT':
                ROC_win = ROC_win + 1
                #print("ROC_wins :" + str(OC_win))
            elif EULCSmatches[i]['tournament_id'] == 684 and EULCSmatches[i]['winner']['name'] == 'FC Schalke 04 Esports':
                S04_win = S04_win + 1
                #print("S04_wins :" + str(S04_win))
            elif EULCSmatches[i]['tournament_id'] == 684 and EULCSmatches[i]['winner']['name'] == 'Misfits Gaming':
                MSF_win = MSF_win + 1
                #print("MSF_wins :" + str(MSF_win))
            elif EULCSmatches[i]['tournament_id'] == 684 and EULCSmatches[i]['winner']['name'] == 'H2K':
                H2K_win = H2K_win + 1
                #print("H2K_wins :" + str(H2K_win))
            elif EULCSmatches[i]['tournament_id'] == 684 and EULCSmatches[i]['winner']['name'] == 'Splyce':
                SPY_win = SPY_win + 1
                #print("SPY_wins :" + str(SPY_win))


        except:
             print('No Data')

    counter = counter + 1

print(EULCSteams)
print("G2 wins:" + str(G2_win))
print("SPY wins:" + str(SPY_win))
print("VIT wins:" + str(VIT_win))
print("UOL wins:" + str(UOL_win))
print("FNC wins:" + str(FNC_win))
print("ROC wins:" + str(ROC_win))
print("S04 wins:" + str(S04_win))
print("MSF wins:" + str(MSF_win))
print("GIA wins:" + str(GIA_win))
print("H2K wins:" + str(H2K_win))



G2_loss = 18 - G2_win
SPY_loss = 18 - SPY_win
VIT_loss = 18 - VIT_win
UOL_loss = 18 - UOL_win
FNC_loss = 18 - FNC_win
ROC_loss = 18 - ROC_win
S04_loss = 18 - S04_win
MSF_loss = 18 - MSF_win
GIA_loss = 18 - GIA_win
H2K_loss = 18 - H2K_win

print("G2 W/L: " + str(G2_win) + "-" + str(G2_loss))
print("SPY W/L: " + str(SPY_win) + "-" + str(SPY_loss))
print("VIT W/L: " + str(VIT_win) + "-" + str(VIT_loss))
print("UOL W/L: " + str(UOL_win) + "-" + str(UOL_loss))
print("FNC W/L: " + str(FNC_win) + "-" + str(FNC_loss))
print("ROC W/L: " + str(ROC_win) + "-" + str(ROC_loss))
print("S04 W/L: " + str(S04_win) + "-" + str(S04_loss))
print("MSF W/L: " + str(MSF_win) + "-" + str(MSF_loss))
print("GIA W/L: " + str(GIA_win) + "-" + str(GIA_loss))
print("H2K W/L: " + str(H2K_win) + "-" + str(H2K_loss))

print("")
print("===========================================")
print("")


NALCSteams = []
NALCSmatches = requests.get(NALCSmatches+api_key)
NALCSmatches = NALCSmatches.json()
#Tournament id for spring split = 684
matchid = NALCSmatches[0]['id']
name = NALCSmatches[0]['name']
winner = NALCSmatches[0]['winner']['name']


C9_win = 0
TSM_win = 0
TL_win = 0
HT_win = 0
CG_win = 0
P1_win = 0
OPT_win = 0
FLY_win = 0
EF_win = 0
GGS_win = 0
CLG_win = 0

for i in range(len(NALCSmatches)):

    try:

        #print(NALCSmatches[i]['id'])
        #print(NALCSmatches[i]['name'])
        #print(NALCSmatches[i]['winner']['name'])
        if NALCSmatches[i]['winner']['name'] not in NALCSteams:
            NALCSteams.append(NALCSmatches[i]['winner']['name'])
        # print('')

        if NALCSmatches[i]['tournament_id'] == 652 and NALCSmatches[i]['winner']['name'] == 'Cloud9':
            C9_win = C9_win + 1
            #print("C9_wins :" + str(C9_win))
        elif NALCSmatches[i]['tournament_id'] == 652 and NALCSmatches[i]['winner']['name'] == 'TSM':
            TSM_win = TSM_win + 1
            #print("TSM_wins :" + str(TSM_win))
        elif NALCSmatches[i]['tournament_id'] == 652 and NALCSmatches[i]['winner']['name'] == 'Team Liquid':
            TL_win = TL_win + 1
            #print("TL_wins :" + str(TL_win))
        elif NALCSmatches[i]['tournament_id'] == 652 and NALCSmatches[i]['winner']['name'] == '100 Thieves':
            HT_win = HT_win + 1
            #print("100T_wins :" + str(100T_win))
        elif NALCSmatches[i]['tournament_id'] == 652 and NALCSmatches[i]['winner']['name'] == 'Clutch Gaming':
            CG_win = CG_win + 1
            #print("P1_wins :" + str(P1_win))
        elif NALCSmatches[i]['tournament_id'] == 652 and NALCSmatches[i]['winner']['name'] == 'Phoenix 1':
            P1_win = P1_win + 1
            #print("ROC_wins :" + str(OC_win))
        elif NALCSmatches[i]['tournament_id'] == 652 and NALCSmatches[i]['winner']['name'] == 'Optic Gaming':
            OPT_win = OPT_win + 1
            #print("OPT_wins :" + str(OPT_win))
        elif NALCSmatches[i]['tournament_id'] == 652 and NALCSmatches[i]['winner']['name'] == 'FlyQuest':
            FLY_win = FLY_win + 1
            #print("FLY_wins :" + str(FLY_win))
        elif NALCSmatches[i]['tournament_id'] == 652 and NALCSmatches[i]['winner']['name'] == 'Echo Fox':
            EF_win = EF_win + 1
            #print("EF_wins :" + str(EF_win))
        elif NALCSmatches[i]['tournament_id'] == 652 and NALCSmatches[i]['winner']['name'] == 'Golden Guardians':
            GGS_win = GGS_win + 1
        elif NALCSmatches[i]['tournament_id'] == 652 and NALCSmatches[i]['winner']['name'] == 'Counter Logic Gaming':
            CLG_win = CLG_win + 1

            #print("GGS_wins :" + str(GGS_win))


    except:
         print('No Data')


print(NALCSteams)
print("C9 wins:" + str(C9_win))
print("TSM wins:" + str(TSM_win))
print("TL wins:" + str(TL_win))
print("HT wins:" + str(HT_win))
print("CG wins:" + str(CG_win))
print("P1 wins:" + str(P1_win))
print("OPT wins:" + str(OPT_win))
print("FLY wins:" + str(FLY_win))
print("EF wins:" + str(EF_win))
print("GGS wins:" + str(GGS_win))
print("CLG wins:" + str(CLG_win))



C9_loss = 18 - C9_win
TSM_loss = 18 - TSM_win
TL_loss = 18 - TL_win
HT_loss = 18 - HT_win
CG_loss = 18 - CG_win
P1_loss = 18 - P1_win
OPT_loss = 18 - OPT_win
FLY_loss = 18 - FLY_win
EF_loss = 18 - EF_win
GGS_loss = 18 - GGS_win
CLG_loss = 18 - CLG_win

print("C9 W/L: " + str(C9_win) + "-" + str(C9_loss))
print("TSM W/L: " + str(TSM_win) + "-" + str(TSM_loss))
print("TL W/L: " + str(TL_win) + "-" + str(TL_loss))
print("HT W/L: " + str(HT_win) + "-" + str(HT_loss))
print("CG W/L: " + str(CG_win) + "-" + str(CG_loss))
print("P1 W/L: " + str(P1_win) + "-" + str(P1_loss))
print("OPT W/L: " + str(OPT_win) + "-" + str(OPT_loss))
print("FLY W/L: " + str(FLY_win) + "-" + str(FLY_loss))
print("EF W/L: " + str(EF_win) + "-" + str(EF_loss))
print("GGS W/L: " + str(GGS_win) + "-" + str(GGS_loss))
print("CLG W/L: " + str(CLG_win) + "-" + str(CLG_loss))

print("")
print("===========================================")
print("")