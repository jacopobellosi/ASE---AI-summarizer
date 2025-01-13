# openapi-client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Generator version: 7.10.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.8+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)



# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    body = 'body_example' # str | 

    try:
        # Generate test
        api_response = api_instance.generate_test_post(body)
        print("The response of DefaultApi->generate_test_post:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->generate_test_post: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**generate_test_post**](docs/DefaultApi.md#generate_test_post) | **POST** /generate_test | Generate test
*DefaultApi* | [**paraphrase_post**](docs/DefaultApi.md#paraphrase_post) | **POST** /paraphrase | Paraphrase text


## Documentation For Models

 - [AssessmentSection](docs/AssessmentSection.md)
 - [AssessmentTest](docs/AssessmentTest.md)
 - [ChoiceInteraction](docs/ChoiceInteraction.md)
 - [Item](docs/Item.md)
 - [ParaphraseRequest](docs/ParaphraseRequest.md)
 - [ParaphraseResponse](docs/ParaphraseResponse.md)
 - [ResponseDeclaration](docs/ResponseDeclaration.md)
 - [SimpleChoice](docs/SimpleChoice.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author



