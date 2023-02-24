# Python library to interact with the ALTERNATIVE platform

## Requirements
Generate an API Token in the platform:
1. From the user page click on API Tokens
2. Create API Tokens
3. Copy and keep API Token, to be used to access private datasets

## Build and install library
In Terminal, execute these commands:
```
git clone https://github.com/ALTERNATIVE-EU/alternative-lib.git
cd alternative-lib
python3 setup.py bdist_wheel
pip install dist/alternative_lib-0.1.0-py3-none-any.whl
```

## Usage
1. Import modules
```
import alternative_lib
from alternative_lib import alternative_client
```
2. Create client
```
alt_client = alternative_client.AlternativeClient()
```
**If you want to be able to access private datasets, you need to have generated an API Token from the platform and use the *api_token* parameter**
```
alt_client = alternative_client.AlternativeClient(
    api_token='your-api-token'
)
```
If you want to connect to another CKAN instance use the *site_url* parameter
```
alt_client = alternative_client.AlternativeClient(
    site_url='site-url-of-the-ckan-instance'
)
```

## Functions
- Get datasets based on metadata
    - *metadata* - (optional) object, containing the metadata, you're searching for in the datasets; if not given - all available datasets are returned; examples of this object can be seen in the tests
    - *datasets* - (optional) array of dataset objects; if not given - all available datasets are checked
    - *not_all_groups* - (optional) if False dataset has to be present in all of the groups in *metadata*, to satisfy the search
    - *not_all_tags* - (optional) if False dataset has to have all the tags in *metadata*, to satisfy the search
```
alt_client.get_datasets(
    metadata=None,
    datasets=None,
    not_all_groups=False,
    not_all_tags=False
)
```
- Download dataset's resource
    - *resource_url* - (required) URL of the resource, can be found in the dataset object under *resources* key
    - *filename* - (required) sets the name of the file, in which the resource is downloaded
    - *path* - (optional) can be used to change the default location of the file
```
alt_client.download_resource(
    resource_url='',
    filename='',
    path='./'
)
```

## Tests
To run tests:
```
python3 setup.py pytest
```
