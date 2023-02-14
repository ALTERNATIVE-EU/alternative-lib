import requests
import ckanapi


class AlternativeClient:

    api_token = ""
    site_url = "https://alternative.ebdfbc2ec9.app.daiteap.com"
    user_agent = "ckanapi/1.0 (+https://alternative.ebdfbc2ec9.app.daiteap.com)"

    def __init__(self, api_token=None, site_url=None):
        if api_token:
            self.api_token = api_token
        if site_url:
            self.site_url = site_url
            self.user_agent = "ckanapi/1.0 (+" + site_url + ")"

    def get_datasets(self, metadata=None, datasets=None, not_all_groups=False, not_all_tags=False):
        # Create CKAN client
        if self.api_token:
            ckanapi_client = ckanapi.RemoteCKAN(
                address=self.site_url,
                user_agent=self.user_agent,
                apikey=self.api_token
            )
        else:
            ckanapi_client = ckanapi.RemoteCKAN(
                address=self.site_url,
                user_agent=self.user_agent
            )

        # Get all datasets
        if not datasets:
            datasets = ckanapi_client.action.package_search(
                include_private=True,
                rows=1000
            )['results']

        results = []

        # Search dataset metadata
        if metadata:
            for dataset in datasets:
                matches_criteria = True

                for key in metadata.keys():
                    if key in dataset:
                        if key == 'extras':
                            for extra in metadata[key]:
                                if extra['key'] not in [x['key'] for x in dataset[key]]:
                                    matches_criteria = False
                                elif isinstance(extra['value'], list):
                                    for value in dataset[key]:
                                        if value['key'] == extra['key'] and value['value'] not in extra['value']:
                                            matches_criteria = False
                                elif extra not in dataset[key]:
                                    matches_criteria = False
                        elif key == 'organization':
                            if isinstance(metadata[key], list):
                                if dataset[key]['title'] not in metadata[key]:
                                    matches_criteria = False
                            elif dataset[key]['title'] != metadata[key]:
                                matches_criteria = False
                        elif key in ['groups', 'tags']:
                            names = [x['display_name'] for x in dataset[key]]
                            if (key == 'groups' and not_all_groups) or (key == 'tags' and not_all_tags):
                                if not bool(set(names).intersection(metadata[key])):
                                    matches_criteria = False
                            else:
                                for value in metadata[key]:
                                    if value not in names:
                                        matches_criteria = False
                        elif isinstance(metadata[key], list):
                            if dataset[key] not in metadata[key]:
                                matches_criteria = False
                        elif dataset[key] != metadata[key]:
                            matches_criteria = False
                    else:
                        matches_criteria = False

                if matches_criteria:
                    results.append(dataset)
        else:
            results = datasets

        return results

    def download_resource(self, resource_url, filename, path='./'):
        # Download resource
        if self.api_token:
            response = requests.get(
                resource_url,
                headers={'Authorization': self.api_token}
            )
        else:
            response = requests.get(resource_url)

        download_url = response.text.split("url='")[1].split("'")[0]
        response = requests.get(download_url)

        # Write to file
        with open(path + filename, "wb") as text_file:
            text_file.write(response.content)
