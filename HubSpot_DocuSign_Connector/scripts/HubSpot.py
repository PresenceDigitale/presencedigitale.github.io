print("HubSpot API")

from hubspot import HubSpot
from hubspot.crm.deals import BasicApi, AssociationsApi, BatchApi, SearchApi, PublicObjectApi

deal_id = '12451140480'

api_client = HubSpot(access_token='')

deal_fetched = api_client.crm.deals.basic_api.get_by_id(deal_id)

print(deal_fetched)
