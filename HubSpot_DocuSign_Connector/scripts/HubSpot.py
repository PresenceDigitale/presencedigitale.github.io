print("HubSpot API")

from hubspot import HubSpot
from hubspot.crm.deals import BasicApi, AssociationsApi, BatchApi, SearchApi, PublicObjectApi

deal_id = '12451140480'

api_client = HubSpot(access_token='pat-na1-8e4a5abf-3f2c-4d2b-9a7d-aec0c869f86b')

deal_fetched = api_client.crm.deals.basic_api.get_by_id(deal_id)

print(deal_fetched)
