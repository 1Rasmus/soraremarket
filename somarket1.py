# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 23:48:32 2020

@author: Rasmus
"""
import requests
import pandas as pd
import time


finished_slug=""
text_file = open("log.txt", "w")
buydata = pd.read_excel (r'buyplayers.xlsx')
buydata['slug']=buydata['slug']+"-"+buydata['rarity']

while True:
    time.sleep(3.3)
    
    ######### Get latest Auction
    data={"requests":[{"indexName":"Card_NewlyListed","params":"highlightPreTag=%3Cais-highlight-0000000000%3E&highlightPostTag=%3C%2Fais-highlight-0000000000%3E&hitsPerPage=20&filters=visible%3D1%20AND%20(rarity%3Arare%20OR%20rarity%3Asuper_rare%20OR%20rarity%3Aunique)&maxValuesPerFacet=10&facets=%5B%22sale.primary%22%2C%22rarity%22%2C%22position%22%2C%22grade%22%2C%22club.long_name%22%2C%22player.display_name%22%2C%22active_league.display_name%22%2C%22country.name_en%22%2C%22player.birth_date_i%22%2C%22stats.percentage_played%22%2C%22stats.goals_per_game%22%2C%22stats.assists_per_game%22%2C%22stats.fouls_balance%22%2C%22stats.yellow_card_per_game%22%2C%22stats.red_card_per_game%22%5D&tagFilters=&facetFilters=%5B%5B%22sale.primary%3Afalse%22%5D%5D&numericFilters=%5B%22grade%3E%3D0%22%2C%22grade%3C%3D20%22%2C%22player.birth_date_i%3E%3D-805561872%22%2C%22player.birth_date_i%3C%3D1119343728%22%2C%22stats.percentage_played%3E%3D0%22%2C%22stats.percentage_played%3C%3D100%22%2C%22stats.goals_per_game%3E%3D0%22%2C%22stats.assists_per_game%3E%3D0%22%2C%22stats.fouls_balance%3E%3D-1%22%2C%22stats.fouls_balance%3C%3D1%22%2C%22stats.yellow_card_per_game%3E%3D0%22%2C%22stats.yellow_card_per_game%3C%3D2%22%2C%22stats.red_card_per_game%3E%3D0%22%2C%22stats.red_card_per_game%3C%3D1%22%5D"},{"indexName":"Card_NewlyListed","params":"highlightPreTag=%3Cais-highlight-0000000000%3E&highlightPostTag=%3C%2Fais-highlight-0000000000%3E&hitsPerPage=1&filters=visible%3D1%20AND%20(rarity%3Arare%20OR%20rarity%3Asuper_rare%20OR%20rarity%3Aunique)&maxValuesPerFacet=10&page=0&attributesToRetrieve=%5B%5D&attributesToHighlight=%5B%5D&attributesToSnippet=%5B%5D&tagFilters=&analytics=false&clickAnalytics=false&facets=sale.primary&numericFilters=%5B%22grade%3E%3D0%22%2C%22grade%3C%3D20%22%2C%22player.birth_date_i%3E%3D-805561872%22%2C%22player.birth_date_i%3C%3D1119343728%22%2C%22stats.percentage_played%3E%3D0%22%2C%22stats.percentage_played%3C%3D100%22%2C%22stats.goals_per_game%3E%3D0%22%2C%22stats.assists_per_game%3E%3D0%22%2C%22stats.fouls_balance%3E%3D-1%22%2C%22stats.fouls_balance%3C%3D1%22%2C%22stats.yellow_card_per_game%3E%3D0%22%2C%22stats.yellow_card_per_game%3C%3D2%22%2C%22stats.red_card_per_game%3E%3D0%22%2C%22stats.red_card_per_game%3C%3D1%22%5D"},{"indexName":"Card_NewlyListed","params":"highlightPreTag=%3Cais-highlight-0000000000%3E&highlightPostTag=%3C%2Fais-highlight-0000000000%3E&hitsPerPage=1&filters=visible%3D1%20AND%20(rarity%3Arare%20OR%20rarity%3Asuper_rare%20OR%20rarity%3Aunique)&maxValuesPerFacet=10&page=0&attributesToRetrieve=%5B%5D&attributesToHighlight=%5B%5D&attributesToSnippet=%5B%5D&tagFilters=&analytics=false&clickAnalytics=false&facets=grade&numericFilters=%5B%22player.birth_date_i%3E%3D-805561872%22%2C%22player.birth_date_i%3C%3D1119343728%22%2C%22stats.percentage_played%3E%3D0%22%2C%22stats.percentage_played%3C%3D100%22%2C%22stats.goals_per_game%3E%3D0%22%2C%22stats.assists_per_game%3E%3D0%22%2C%22stats.fouls_balance%3E%3D-1%22%2C%22stats.fouls_balance%3C%3D1%22%2C%22stats.yellow_card_per_game%3E%3D0%22%2C%22stats.yellow_card_per_game%3C%3D2%22%2C%22stats.red_card_per_game%3E%3D0%22%2C%22stats.red_card_per_game%3C%3D1%22%5D&facetFilters=%5B%5B%22sale.primary%3Afalse%22%5D%5D"},{"indexName":"Card_NewlyListed","params":"highlightPreTag=%3Cais-highlight-0000000000%3E&highlightPostTag=%3C%2Fais-highlight-0000000000%3E&hitsPerPage=1&filters=visible%3D1%20AND%20(rarity%3Arare%20OR%20rarity%3Asuper_rare%20OR%20rarity%3Aunique)&maxValuesPerFacet=10&page=0&attributesToRetrieve=%5B%5D&attributesToHighlight=%5B%5D&attributesToSnippet=%5B%5D&tagFilters=&analytics=false&clickAnalytics=false&facets=player.birth_date_i&numericFilters=%5B%22grade%3E%3D0%22%2C%22grade%3C%3D20%22%2C%22stats.percentage_played%3E%3D0%22%2C%22stats.percentage_played%3C%3D100%22%2C%22stats.goals_per_game%3E%3D0%22%2C%22stats.assists_per_game%3E%3D0%22%2C%22stats.fouls_balance%3E%3D-1%22%2C%22stats.fouls_balance%3C%3D1%22%2C%22stats.yellow_card_per_game%3E%3D0%22%2C%22stats.yellow_card_per_game%3C%3D2%22%2C%22stats.red_card_per_game%3E%3D0%22%2C%22stats.red_card_per_game%3C%3D1%22%5D&facetFilters=%5B%5B%22sale.primary%3Afalse%22%5D%5D"},{"indexName":"Card_NewlyListed","params":"highlightPreTag=%3Cais-highlight-0000000000%3E&highlightPostTag=%3C%2Fais-highlight-0000000000%3E&hitsPerPage=1&filters=visible%3D1%20AND%20(rarity%3Arare%20OR%20rarity%3Asuper_rare%20OR%20rarity%3Aunique)&maxValuesPerFacet=10&page=0&attributesToRetrieve=%5B%5D&attributesToHighlight=%5B%5D&attributesToSnippet=%5B%5D&tagFilters=&analytics=false&clickAnalytics=false&facets=stats.percentage_played&numericFilters=%5B%22grade%3E%3D0%22%2C%22grade%3C%3D20%22%2C%22player.birth_date_i%3E%3D-805561872%22%2C%22player.birth_date_i%3C%3D1119343728%22%2C%22stats.goals_per_game%3E%3D0%22%2C%22stats.assists_per_game%3E%3D0%22%2C%22stats.fouls_balance%3E%3D-1%22%2C%22stats.fouls_balance%3C%3D1%22%2C%22stats.yellow_card_per_game%3E%3D0%22%2C%22stats.yellow_card_per_game%3C%3D2%22%2C%22stats.red_card_per_game%3E%3D0%22%2C%22stats.red_card_per_game%3C%3D1%22%5D&facetFilters=%5B%5B%22sale.primary%3Afalse%22%5D%5D"},{"indexName":"Card_NewlyListed","params":"highlightPreTag=%3Cais-highlight-0000000000%3E&highlightPostTag=%3C%2Fais-highlight-0000000000%3E&hitsPerPage=1&filters=visible%3D1%20AND%20(rarity%3Arare%20OR%20rarity%3Asuper_rare%20OR%20rarity%3Aunique)&maxValuesPerFacet=10&page=0&attributesToRetrieve=%5B%5D&attributesToHighlight=%5B%5D&attributesToSnippet=%5B%5D&tagFilters=&analytics=false&clickAnalytics=false&facets=stats.goals_per_game&numericFilters=%5B%22grade%3E%3D0%22%2C%22grade%3C%3D20%22%2C%22player.birth_date_i%3E%3D-805561872%22%2C%22player.birth_date_i%3C%3D1119343728%22%2C%22stats.percentage_played%3E%3D0%22%2C%22stats.percentage_played%3C%3D100%22%2C%22stats.assists_per_game%3E%3D0%22%2C%22stats.fouls_balance%3E%3D-1%22%2C%22stats.fouls_balance%3C%3D1%22%2C%22stats.yellow_card_per_game%3E%3D0%22%2C%22stats.yellow_card_per_game%3C%3D2%22%2C%22stats.red_card_per_game%3E%3D0%22%2C%22stats.red_card_per_game%3C%3D1%22%5D&facetFilters=%5B%5B%22sale.primary%3Afalse%22%5D%5D"},{"indexName":"Card_NewlyListed","params":"highlightPreTag=%3Cais-highlight-0000000000%3E&highlightPostTag=%3C%2Fais-highlight-0000000000%3E&hitsPerPage=1&filters=visible%3D1%20AND%20(rarity%3Arare%20OR%20rarity%3Asuper_rare%20OR%20rarity%3Aunique)&maxValuesPerFacet=10&page=0&attributesToRetrieve=%5B%5D&attributesToHighlight=%5B%5D&attributesToSnippet=%5B%5D&tagFilters=&analytics=false&clickAnalytics=false&facets=stats.assists_per_game&numericFilters=%5B%22grade%3E%3D0%22%2C%22grade%3C%3D20%22%2C%22player.birth_date_i%3E%3D-805561872%22%2C%22player.birth_date_i%3C%3D1119343728%22%2C%22stats.percentage_played%3E%3D0%22%2C%22stats.percentage_played%3C%3D100%22%2C%22stats.goals_per_game%3E%3D0%22%2C%22stats.fouls_balance%3E%3D-1%22%2C%22stats.fouls_balance%3C%3D1%22%2C%22stats.yellow_card_per_game%3E%3D0%22%2C%22stats.yellow_card_per_game%3C%3D2%22%2C%22stats.red_card_per_game%3E%3D0%22%2C%22stats.red_card_per_game%3C%3D1%22%5D&facetFilters=%5B%5B%22sale.primary%3Afalse%22%5D%5D"},{"indexName":"Card_NewlyListed","params":"highlightPreTag=%3Cais-highlight-0000000000%3E&highlightPostTag=%3C%2Fais-highlight-0000000000%3E&hitsPerPage=1&filters=visible%3D1%20AND%20(rarity%3Arare%20OR%20rarity%3Asuper_rare%20OR%20rarity%3Aunique)&maxValuesPerFacet=10&page=0&attributesToRetrieve=%5B%5D&attributesToHighlight=%5B%5D&attributesToSnippet=%5B%5D&tagFilters=&analytics=false&clickAnalytics=false&facets=stats.fouls_balance&numericFilters=%5B%22grade%3E%3D0%22%2C%22grade%3C%3D20%22%2C%22player.birth_date_i%3E%3D-805561872%22%2C%22player.birth_date_i%3C%3D1119343728%22%2C%22stats.percentage_played%3E%3D0%22%2C%22stats.percentage_played%3C%3D100%22%2C%22stats.goals_per_game%3E%3D0%22%2C%22stats.assists_per_game%3E%3D0%22%2C%22stats.yellow_card_per_game%3E%3D0%22%2C%22stats.yellow_card_per_game%3C%3D2%22%2C%22stats.red_card_per_game%3E%3D0%22%2C%22stats.red_card_per_game%3C%3D1%22%5D&facetFilters=%5B%5B%22sale.primary%3Afalse%22%5D%5D"},{"indexName":"Card_NewlyListed","params":"highlightPreTag=%3Cais-highlight-0000000000%3E&highlightPostTag=%3C%2Fais-highlight-0000000000%3E&hitsPerPage=1&filters=visible%3D1%20AND%20(rarity%3Arare%20OR%20rarity%3Asuper_rare%20OR%20rarity%3Aunique)&maxValuesPerFacet=10&page=0&attributesToRetrieve=%5B%5D&attributesToHighlight=%5B%5D&attributesToSnippet=%5B%5D&tagFilters=&analytics=false&clickAnalytics=false&facets=stats.yellow_card_per_game&numericFilters=%5B%22grade%3E%3D0%22%2C%22grade%3C%3D20%22%2C%22player.birth_date_i%3E%3D-805561872%22%2C%22player.birth_date_i%3C%3D1119343728%22%2C%22stats.percentage_played%3E%3D0%22%2C%22stats.percentage_played%3C%3D100%22%2C%22stats.goals_per_game%3E%3D0%22%2C%22stats.assists_per_game%3E%3D0%22%2C%22stats.fouls_balance%3E%3D-1%22%2C%22stats.fouls_balance%3C%3D1%22%2C%22stats.red_card_per_game%3E%3D0%22%2C%22stats.red_card_per_game%3C%3D1%22%5D&facetFilters=%5B%5B%22sale.primary%3Afalse%22%5D%5D"},{"indexName":"Card_NewlyListed","params":"highlightPreTag=%3Cais-highlight-0000000000%3E&highlightPostTag=%3C%2Fais-highlight-0000000000%3E&hitsPerPage=1&filters=visible%3D1%20AND%20(rarity%3Arare%20OR%20rarity%3Asuper_rare%20OR%20rarity%3Aunique)&maxValuesPerFacet=10&page=0&attributesToRetrieve=%5B%5D&attributesToHighlight=%5B%5D&attributesToSnippet=%5B%5D&tagFilters=&analytics=false&clickAnalytics=false&facets=stats.red_card_per_game&numericFilters=%5B%22grade%3E%3D0%22%2C%22grade%3C%3D20%22%2C%22player.birth_date_i%3E%3D-805561872%22%2C%22player.birth_date_i%3C%3D1119343728%22%2C%22stats.percentage_played%3E%3D0%22%2C%22stats.percentage_played%3C%3D100%22%2C%22stats.goals_per_game%3E%3D0%22%2C%22stats.assists_per_game%3E%3D0%22%2C%22stats.fouls_balance%3E%3D-1%22%2C%22stats.fouls_balance%3C%3D1%22%2C%22stats.yellow_card_per_game%3E%3D0%22%2C%22stats.yellow_card_per_game%3C%3D2%22%5D&facetFilters=%5B%5B%22sale.primary%3Afalse%22%5D%5D"}]}
    r = requests.post('https://7z0z8pasdy-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(3.35.1)%3B%20Browser%20(lite)%3B%20JS%20Helper%20(3.1.1)%3B%20react%20(16.12.0)%3B%20react-instantsearch%20(6.4.0)&x-algolia-application-id=7Z0Z8PASDY&x-algolia-api-key=2fb5f7ca18102716624d1820bb58cc14', json=data)
    if r.status_code != 200:
        print ("!!!Connection failed... ",r.status_code)
        time.sleep(300.0)
        continue
    parsed_response = r.json()
    slug=parsed_response['results'][0].get('hits')[0].get('objectID')
    
    
    ######## Get Card's Info
    if slug == finished_slug:
        continue
        
    finished_slug=slug
    query = """
    {card
         (slug:"""+'"'+ slug+'"'+""")
         {
        rarity
        price
        player
         {
        displayName
        cardSupply
        {
             rare
             superRare
             unique
        }
         }
         }
       }
    """
        
    r = requests.post('https://api.sorare.com/graphql', json={'query': query})
    if r.status_code != 200:
        print ("!!!Connection failed... ",r.status_code)
        time.sleep(300.0)
        continue
    slugdata=r.json()
                
    rarity=slugdata['data']['card']['rarity']        
    price=int(slugdata['data']['card']['price'])/1000000000000000000
    name=slugdata['data']['card']['player']['displayName']
    #print ("Slug: ",slug)
    #print ("Name: ",name)
    #print ("Scarcity: ",rarity)
    #print ("Preis :",price)
        
    if rarity =="unique":
        amount=slugdata['data']['card']['player']['cardSupply'][0]['unique']
        slug_split=slug.split('unique')[0]
    if rarity =="super_rare":
        amount=slugdata['data']['card']['player']['cardSupply'][0]['superRare']
        slug_split=slug.split('super_rare')[0]
    if rarity =="rare":
        amount=slugdata['data']['card']['player']['cardSupply'][0]['rare']
        slug_split=slug.split('rare')[0]
        
    ######### Check if Card is on demand list and alert
    if buydata['slug'].str.contains(slug_split+rarity).any():
        buy_price=buydata[buydata['slug'].str.match(slug_split+rarity)].buyprice.item()
        if buy_price >=price:
            print ('############## Buylist #############'+'\n'+slug+'\n'+rarity+'\n'+str(buy_price)+'\n'+str(price)+'\n'+'############## Buylist #############')
            continue
        
    
    ######### Get Card's average sale price
    df=pd.DataFrame (columns=['price', 'date'])
    for i in range (amount):
                       
        query = """
        {card
             (slug:"""+'"'+ slug_split+rarity+"-"+str(i+1)+'"'+""")
             {
            userOwnerWithRate
            {
            price
            from
            }
             }
        }
        """
        r = requests.post('https://api.sorare.com/graphql', json={'query': query})
        if r.status_code != 200:
            print ("!!!Connection failed... ",r.status_code)
            time.sleep(300.0)
            continue
        avgpricedata=r.json()
        if avgpricedata['data']['card']['userOwnerWithRate'] is not None:
            hist_price=int(avgpricedata['data']['card']['userOwnerWithRate']['price'])/1000000000000000000
            hist_date=avgpricedata['data']['card']['userOwnerWithRate']['from']
            df.loc[i,'price']=hist_price
            df.loc[i,'date']=hist_date
            time.sleep (0.1)
        
        
    ######### Alert if price > average price
        
    df = df[df.price != 0]
    if len(df) <2:
        continue
    df=df.sort_values(by='date', ascending=False)
    avg_price=df['price'].head(2).mean()
    #print ("Avg Preis: ",avg_price)
    if (price*1.1) <= avg_price:
        text_file.write("Player: "+slug+ '\n'+ "Rarity: "+rarity +'\n'+"Avg_Price: "+ str(avg_price) +'\n'+"Buy_Price: "+str(price)+ '\n')
        print ('###########################'+'\n'+slug+'\n'+rarity+'\n'+str(avg_price)+'\n'+str(price)+'\n'+'###########################')
    
    
