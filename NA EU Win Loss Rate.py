
import requests
import pandas as pd
import json
import numpy
import pprint as pp
from config import api_key

# Get PandaScore
# series_old = "https://api.pandascore.co/series?token="

# Need to store teamIDs, Description

leagues = "https://api.pandascore.co/videogames/1/leagues?year=2018&token="
# ID's for consideration -
# EU LCS id: 290
# NA LCS id: 289

series = "https://api.pandascore.co/videogames/1/series?year=2018&token="
seriesmatches = "https://api.pandascore.co/videogames/1/series/1343/matches?year=2018&token="
tournaments = "https://api.pandascore.co/videogames/1/tournaments?token="
teams = "https://api.pandascore.co/videogames/1/teams?token="
videogames = "https://api.pandascore.co/videogames/1?token="

EULCSmatches = "https://api.pandascore.co/tournaments/684/matches?page="
NALCSmatches = "https://api.pandascore.co/tournaments/652/matches?page="

token = "&token="


# response = requests.get(leagues+api_key)
# league_id = response.json()
# pydata = json.dumps(league_id)
# pydata = pd.read_json(pydata)
# league_id = pydata[['id','name']]
# values=[289,290]
# NAEULCSLeague_id = league_id.loc[league_id['id'].isin(values)]
# print('League_ID')
# pp.pprint(NAEULCSLeague_id)
# print('')
# print('=========================================')
# print('')
#
# #Get Series ID for NALCS and EULCS Spring
#     #EULCS serie_id = 1343
#     #NALCS serie_id = 1333
# series = requests.get(series+api_key)
# series = series.json()
# series = json.dumps(series)
# series = pd.read_json(series)
# series_id = series[['id','name','season','league_id','year']]
#
# print('Series_ID')
# pp.pprint(series_id)
# print('')
# print('========================================')
# print('')

# Get Match IDs for EULCS
# Get Win Count By Team
# Get Loss Count By Team
# Get List of Teams

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
G2_loss = 0
SPY_loss = 0
VIT_loss = 0
UOL_loss = 0
FNC_loss = 0
ROC_loss = 0
S04_loss = 0
MSF_loss = 0
GIA_loss = 0
H2K_loss = 0

pages = ['1', '2']
euMatches = []

for page in pages:
    url = EULCSmatches + page + token + api_key
    response = requests.get(url)
    data = response.json()
    euMatches.append(data)
    # Tournament id for spring split = 684
    # matchid = EULCSmatches[0]['id']
    # name = EULCSmatches[0]['name']
    # winner = EULCSmatches[0]['winner']['name']

for j in range(0, 2):
    for i in range(len(euMatches[j])):

        try:
            # print('')
            # print(EULCSmatches[i]['id'])
            # print(EULCSmatches[i]['name'])
            # print(EULCSmatches[i]['winner']['name'])
            if euMatches[j][i]['winner']['name'] not in EULCSteams:
                EULCSteams.append(euMatches[j][i]['winner']['name'])
            # print('')
            # Wins
            if euMatches[j][i]['tournament_id'] == 684 and euMatches[j][i]['winner']['name'] == 'G2 Esports':
                G2_win = G2_win + 1
                # print("G2_wins :" + str(G2_win))
            elif euMatches[j][i]['tournament_id'] == 684 and euMatches[j][i]['winner']['name'] == 'Splyce':
                SPY_win = SPY_win + 1
                # print("SPY_wins :" + str(SPY_win))
            elif euMatches[j][i]['tournament_id'] == 684 and euMatches[j][i]['winner']['name'] == 'Unicorns of Love':
                UOL_win = UOL_win + 1
                # print("UOL_wins :" + str(UOL_win))
            elif euMatches[j][i]['tournament_id'] == 684 and euMatches[j][i]['winner']['name'] == 'Vitality':
                VIT_win = VIT_win + 1
                # print("VIT_wins :" + str(VIT_win))
            elif euMatches[j][i]['tournament_id'] == 684 and euMatches[j][i]['winner']['name'] == 'Fnatic':
                FNC_win = FNC_win + 1
                # print("FNC_wins :" + str(FNC_win))
            elif euMatches[j][i]['tournament_id'] == 684 and euMatches[j][i]['winner']['name'] == 'ROCCAT':
                ROC_win = ROC_win + 1
                # print("ROC_wins :" + str(OC_win))
            elif euMatches[j][i]['tournament_id'] == 684 and euMatches[j][i]['winner'][
                'name'] == 'FC Schalke 04 Esports':
                S04_win = S04_win + 1
                # print("S04_wins :" + str(S04_win))
            elif euMatches[j][i]['tournament_id'] == 684 and euMatches[j][i]['winner']['name'] == 'Misfits Gaming':
                MSF_win = MSF_win + 1
                # print("MSF_wins :" + str(MSF_win))
            elif euMatches[j][i]['tournament_id'] == 684 and euMatches[j][i]['winner']['name'] == 'H2K':
                H2K_win = H2K_win + 1
                # print("H2K_wins :" + str(H2K_win))
            elif euMatches[j][i]['tournament_id'] == 684 and euMatches[j][i]['winner']['name'] == 'Giants':
                GIA_win = GIA_win + 1
            # Losses
            if euMatches[j][i]['tournament_id'] == 684 and (
                    euMatches[j][i]['opponents'][0]['opponent']['name'] == 'G2 Esports' or
                    euMatches[j][i]['opponents'][1]['opponent']['name'] == 'G2 Esports') \
                    and euMatches[j][i]['winner']['name'] != 'G2 Esports':
                G2_loss = G2_loss + 1
                # print("G2_losss :" + str(G2_loss))
            elif euMatches[j][i]['tournament_id'] == 684 and (
                    euMatches[j][i]['opponents'][0]['opponent']['name'] == 'Splyce' or
                    euMatches[j][i]['opponents'][1]['opponent']['name'] == 'Splyce') \
                    and euMatches[j][i]['winner']['name'] != 'Splyce':
                SPY_loss = SPY_loss + 1
                # print("SPY_losss :" + str(SPY_loss))
            elif euMatches[j][i]['tournament_id'] == 684 and (
                    euMatches[j][i]['opponents'][0]['opponent']['name'] == 'Unicorns of Love' or
                    euMatches[j][i]['opponents'][1]['opponent']['name'] == 'Unicorns of Love') \
                    and euMatches[j][i]['winner']['name'] != 'Unicorns of Love':
                UOL_loss = UOL_loss + 1
                # print("UOL_losss :" + str(UOL_loss))
            elif euMatches[j][i]['tournament_id'] == 684 and (
                    euMatches[j][i]['opponents'][0]['opponent']['name'] == 'Vitality' or
                    euMatches[j][i]['opponents'][1]['opponent']['name'] == 'Vitality') \
                    and euMatches[j][i]['winner']['name'] != 'Vitality':
                VIT_loss = VIT_loss + 1
                # print("VIT_losss :" + str(VIT_loss))
            elif euMatches[j][i]['tournament_id'] == 684 and (
                    euMatches[j][i]['opponents'][0]['opponent']['name'] == 'Fnatic' or
                    euMatches[j][i]['opponents'][1]['opponent']['name'] == 'Fnatic') \
                    and euMatches[j][i]['winner']['name'] != 'Fnatic':
                FNC_loss = FNC_loss + 1
                # print("FNC_losss :" + str(FNC_loss))
            elif euMatches[j][i]['tournament_id'] == 684 and (
                    euMatches[j][i]['opponents'][0]['opponent']['name'] == 'ROCCAT' or
                    euMatches[j][i]['opponents'][1]['opponent']['name'] == 'ROCCAT') \
                    and euMatches[j][i]['winner']['name'] != 'ROCCAT':
                ROC_loss = ROC_loss + 1
                # print("ROC_losss :" + str(OC_loss))
            elif euMatches[j][i]['tournament_id'] == 684 and (
                    euMatches[j][i]['opponents'][0]['opponent']['name'] == 'FC Schalke 04 Esports' or
                    euMatches[j][i]['opponents'][1]['opponent']['name'] == 'FC Schalke 04 Esports') \
                    and euMatches[j][i]['winner']['name'] != 'FC Schalke 04 Esports':
                S04_loss = S04_loss + 1
                # print("S04_losss :" + str(S04_loss))
            elif euMatches[j][i]['tournament_id'] == 684 and (
                    euMatches[j][i]['opponents'][0]['opponent']['name'] == 'Misfits Gaming' or
                    euMatches[j][i]['opponents'][1]['opponent']['name'] == 'Misfits Gaming') \
                    and euMatches[j][i]['winner']['name'] != 'Misfits Gaming':
                MSF_loss = MSF_loss + 1
                # print("MSF_losss :" + str(MSF_loss))
            elif euMatches[j][i]['tournament_id'] == 684 and (
                    euMatches[j][i]['opponents'][0]['opponent']['name'] == 'H2K' or
                    euMatches[j][i]['opponents'][1]['opponent']['name'] == 'H2K') \
                    and euMatches[j][i]['winner']['name'] != 'H2K':
                H2K_loss = H2K_loss + 1
                # print("H2K_losss :" + str(H2K_loss))
            elif euMatches[j][i]['tournament_id'] == 684 and (
                    euMatches[j][i]['opponents'][0]['opponent']['name'] == 'Giants' or
                    euMatches[j][i]['opponents'][1]['opponent']['name'] == 'Giants') \
                    and euMatches[j][i]['winner']['name'] != 'Giants':
                GIA_loss = GIA_loss + 1
                # print("SPY_losss :" + str(SPY_loss))


        except:
            print('No Data')

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
# NALCSmatches = requests.get(NALCSmatches+api_key)
# NALCSmatches = NALCSmatches.json()
# #Tournament id for spring split = 684

C9_win = 0
TSM_win = 0
TL_win = 0
HT_win = 0
CG_win = 0
OPT_win = 0
FLY_win = 0
EF_win = 0
GGS_win = 0
CLG_win = 0
C9_loss = 0
TSM_loss = 0
TL_loss = 0
HT_loss = 0
CG_loss = 0
OPT_loss = 0
FLY_loss = 0
EF_loss = 0
GGS_loss = 0
CLG_loss = 0

naMatches = []

for page in pages:
    url = NALCSmatches + page + token + api_key
    response = requests.get(url)
    data = response.json()
    naMatches.append(data)

for j in range(0, 2):
    for i in range(len(naMatches[j])):

        try:
            # print(NALCSmatches[i]['id'])
            # print(NALCSmatches[i]['name'])
            # print(NALCSmatches[i]['winner']['name'])
            if naMatches[j][i]['winner']['name'] not in NALCSteams:
                NALCSteams.append(naMatches[j][i]['winner']['name'])
            # print('')
            # losses
            if naMatches[j][i]['tournament_id'] == 652 and (
                    naMatches[j][i]['opponents'][0]['opponent']['name'] == 'Cloud9' or
                    naMatches[j][i]['opponents'][1]['opponent']['name'] == 'Cloud9') \
                    and naMatches[j][i]['winner']['name'] != 'Cloud9':
                C9_loss = C9_loss + 1
                # print("C9_losss :" + str(C9_loss))
            elif naMatches[j][i]['tournament_id'] == 652 and (
                    naMatches[j][i]['opponents'][0]['opponent']['name'] == 'TSM' or
                    naMatches[j][i]['opponents'][1]['opponent']['name'] == 'TSM') \
                    and naMatches[j][i]['winner']['name'] != 'TSM':
                TSM_loss = TSM_loss + 1
                # print("TSM_losss :" + str(TSM_loss))
            elif naMatches[j][i]['tournament_id'] == 652 and (
                    naMatches[j][i]['opponents'][0]['opponent']['name'] == 'Team Liquid' or
                    naMatches[j][i]['opponents'][1]['opponent']['name'] == 'Team Liquid') \
                    and naMatches[j][i]['winner']['name'] != 'Team Liquid':
                TL_loss = TL_loss + 1
                # print("TL_losss :" + str(TL_loss))
            elif naMatches[j][i]['tournament_id'] == 652 and (
                    naMatches[j][i]['opponents'][0]['opponent']['name'] == '100 Thieves' or
                    naMatches[j][i]['opponents'][1]['opponent']['name'] == '100 Thieves') \
                    and naMatches[j][i]['winner']['name'] != '100 Thieves':
                HT_loss = HT_loss + 1
                # print("100T_losss :" + str(100T_loss))
            elif naMatches[j][i]['tournament_id'] == 652 and (
                    naMatches[j][i]['opponents'][0]['opponent']['name'] == 'Clutch Gaming' or
                    naMatches[j][i]['opponents'][1]['opponent']['name'] == 'Clutch Gaming') \
                    and naMatches[j][i]['winner']['name'] != 'Clutch Gaming':
                CG_loss = CG_loss + 1
                # print("ROC_losss :" + str(OC_loss))
            elif naMatches[j][i]['tournament_id'] == 652 and (
                    naMatches[j][i]['opponents'][0]['opponent']['name'] == 'OpTic Gaming' or
                    naMatches[j][i]['opponents'][1]['opponent']['name'] == 'OpTic Gaming') \
                    and naMatches[j][i]['winner']['name'] != 'OpTic Gaming':
                OPT_loss = OPT_loss + 1
                # print("OPT_losss :" + str(OPT_loss))
            elif naMatches[j][i]['tournament_id'] == 652 and (
                    naMatches[j][i]['opponents'][0]['opponent']['name'] == 'FlyQuest' or
                    naMatches[j][i]['opponents'][1]['opponent']['name'] == 'FlyQuest') \
                    and naMatches[j][i]['winner']['name'] != 'FlyQuest':
                FLY_loss = FLY_loss + 1
                # print("FLY_losss :" + str(FLY_loss))
            elif naMatches[j][i]['tournament_id'] == 652 and (
                    naMatches[j][i]['opponents'][0]['opponent']['name'] == 'Echo Fox' or
                    naMatches[j][i]['opponents'][1]['opponent']['name'] == 'Echo Fox') \
                    and naMatches[j][i]['winner']['name'] != 'Echo Fox':
                EF_loss = EF_loss + 1
                # print("EF_losss :" + str(EF_loss))
            elif naMatches[j][i]['tournament_id'] == 652 and (
                    naMatches[j][i]['opponents'][0]['opponent']['name'] == 'Golden Guardians' or
                    naMatches[j][i]['opponents'][1]['opponent']['name'] == 'Golden Guardians') \
                    and naMatches[j][i]['winner']['name'] != 'Golden Guardians':
                GGS_loss = GGS_loss + 1
            elif naMatches[j][i]['tournament_id'] == 652 and (
                    naMatches[j][i]['opponents'][0]['opponent']['name'] == 'Counter Logic Gaming' or
                    naMatches[j][i]['opponents'][1]['opponent']['name'] == 'Counter Logic Gaming') \
                    and naMatches[j][i]['winner']['name'] != 'Counter Logic Gaming':
                CLG_loss = CLG_loss + 1
            # wins
            if naMatches[j][i]['tournament_id'] == 652 and naMatches[j][i]['winner']['name'] == 'Cloud9':
                C9_win = C9_win + 1
                # print("C9_wins :" + str(C9_win))
            elif naMatches[j][i]['tournament_id'] == 652 and naMatches[j][i]['winner']['name'] == 'TSM':
                TSM_win = TSM_win + 1
                # print("TSM_wins :" + str(TSM_win))
            elif naMatches[j][i]['tournament_id'] == 652 and naMatches[j][i]['winner']['name'] == 'Team Liquid':
                TL_win = TL_win + 1
                # print("TL_wins :" + str(TL_win))
            elif naMatches[j][i]['tournament_id'] == 652 and naMatches[j][i]['winner']['name'] == '100 Thieves':
                HT_win = HT_win + 1
                # print("100T_wins :" + str(100T_win))
            elif naMatches[j][i]['tournament_id'] == 652 and naMatches[j][i]['winner']['name'] == 'Clutch Gaming':
                CG_win = CG_win + 1
                # print("ROC_wins :" + str(OC_win))
            elif naMatches[j][i]['tournament_id'] == 652 and naMatches[j][i]['winner']['name'] == 'OpTic Gaming':
                OPT_win = OPT_win + 1
                # print("OPT_wins :" + str(OPT_win))
            elif naMatches[j][i]['tournament_id'] == 652 and naMatches[j][i]['winner']['name'] == 'FlyQuest':
                FLY_win = FLY_win + 1
                # print("FLY_wins :" + str(FLY_win))
            elif naMatches[j][i]['tournament_id'] == 652 and naMatches[j][i]['winner']['name'] == 'Echo Fox':
                EF_win = EF_win + 1
                # print("EF_wins :" + str(EF_win))
            elif naMatches[j][i]['tournament_id'] == 652 and naMatches[j][i]['winner']['name'] == 'Golden Guardians':
                GGS_win = GGS_win + 1
            elif naMatches[j][i]['tournament_id'] == 652 and naMatches[j][i]['winner'][
                'name'] == 'Counter Logic Gaming':
                CLG_win = CLG_win + 1

                # print("GGS_wins :" + str(GGS_win))


        except:
            print('No Data')

print(NALCSteams)
print("C9 wins:" + str(C9_win))
print("TSM wins:" + str(TSM_win))
print("TL wins:" + str(TL_win))
print("100T wins:" + str(HT_win))
print("CG wins:" + str(CG_win))
print("OPT wins:" + str(OPT_win))
print("FLY wins:" + str(FLY_win))
print("EF wins:" + str(EF_win))
print("GGS wins:" + str(GGS_win))
print("CLG wins:" + str(CLG_win))

print("C9 W/L: " + str(C9_win) + "-" + str(C9_loss))
print("TSM W/L: " + str(TSM_win) + "-" + str(TSM_loss))
print("TL W/L: " + str(TL_win) + "-" + str(TL_loss))
print("HT W/L: " + str(HT_win) + "-" + str(HT_loss))
print("CG W/L: " + str(CG_win) + "-" + str(CG_loss))
print("OPT W/L: " + str(OPT_win) + "-" + str(OPT_loss))
print("FLY W/L: " + str(FLY_win) + "-" + str(FLY_loss))
print("EF W/L: " + str(EF_win) + "-" + str(EF_loss))
print("GGS W/L: " + str(GGS_win) + "-" + str(GGS_loss))
print("CLG W/L: " + str(CLG_win) + "-" + str(CLG_loss))

print("")
print("===========================================")
print("")

# Construct DataFrame
d = {'Region': ['Europe',
                'Europe',
                'Europe',
                'Europe',
                'Europe',
                'Europe',
                'Europe',
                'Europe',
                'Europe',
                'Europe',
                'North America',
                'North America',
                'North America',
                'North America',
                'North America',
                'North America',
                'North America',
                'North America',
                'North America',
                'North America',
                ],

     'Wins': [G2_win,
              SPY_win,
              VIT_win,
              UOL_win,
              FNC_win,
              ROC_win,
              S04_win,
              MSF_win,
              GIA_win,
              H2K_win,
              C9_win,
              TSM_win,
              TL_win,
              HT_win,
              CG_win,
              OPT_win,
              FLY_win,
              EF_win,
              GGS_win,
              CLG_win
              ],
     'Losses': [G2_loss,
                SPY_loss,
                VIT_loss,
                UOL_loss,
                FNC_loss,
                ROC_loss,
                S04_loss,
                MSF_loss,
                GIA_loss,
                H2K_loss,
                C9_loss,
                TSM_loss,
                TL_loss,
                HT_loss,
                CG_loss,
                OPT_loss,
                FLY_loss,
                EF_loss,
                GGS_loss,
                CLG_loss
                ]
     }

index = ['G2 Esports', 'Splyce', 'Vitality', 'Unicorns of Love', 'Fnatic', 'ROCCAT', 'FC Schalke 04 Esports',
         'Misfits Gaming', 'Giants', 'H2K',
         'Cloud9', 'TSM', 'Team Liquid', '100 Thieves', 'Clutch Gaming', 'OpTic Gaming', 'FlyQuest', 'Echo Fox',
         'Golden Guardians', 'Counter Logic Gaming']

df = pd.DataFrame(d, index=index)
df = df[['Region', 'Wins', 'Losses']]
print(df)
df.to_csv('WinLossRates.csv')
