mykey = '06cd112f-ac86-4ff0-bb5e-8771de1a7668'
import RiotConsts as Consts
from RiotAPI import RiotAPI

def main():
    api = RiotAPI(mykey)
    choice = raw_input("Input 1 for summoner name or 2 for champion lore \n")
    if choice=='1':
        myname = raw_input("Input summoner name, no caps \n")
        r = api.get_summoner_by_name(myname)
        #myid = r[myname]['id']
        print r
    elif choice=='2':
        champion_name = raw_input("Input champion name \n")
        r = api.get_champion_data()
        print r['data'][champion_name]['lore']
    else:
        main()

if __name__ == "__main__":
    main()
