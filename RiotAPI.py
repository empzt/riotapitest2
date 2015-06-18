import RiotConsts as Consts

class RiotAPI(object):

    def __init__(self, api_key, region=Consts.REGIONS['europe_west']):
        self.api_key = api_key
        self.region = region
        
    def _request(self, api_url, params):
    
    
