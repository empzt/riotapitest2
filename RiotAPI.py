import requests
import RiotConsts as Consts


class RiotAPI(object):
    def __init__(self, api_key, region=Consts.REGIONS['europe_west']):
        self.api_key = api_key
        self.region = region

    def _request(self, api_url, params={}):
        args = {'api_key': self.api_key}

        for key, value in params.items():
            if key not in args:
                args[key] = value

        response = requests.get(
            Consts.URL['base'].format(
                proxy=self.region,
                region=self.region,
                url=api_url
            ),
            params=args
        )
        print response.url
        return response.json()

    def _staticrequest(self, api_url, params={'champData': 'all'}):

        args = {'api_key': self.api_key}

        for key, value in params.items():
            if key not in args:
                args[key] = value

        response = requests.get(
            Consts.URL['staticbase'].format(
                region=self.region,
                url=api_url
            ),
            params=args
        )

        print response.url
        return response.json()

    def get_summoner_by_name(self, name):
        api_url = Consts.URL['summoner_by_name'].format(
            version=Consts.API_VERSIONS['summoner'],
            names=name
        )
        return self._request(api_url)

    def get_champion_data(self):
        api_url = Consts.URL['champion_info'].format(
            version=Consts.API_VERSIONS['champion_info']
        )
        return self._staticrequest(api_url)
