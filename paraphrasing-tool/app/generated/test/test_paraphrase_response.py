# coding: utf-8

"""
    Paraphrasing Tool API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.paraphrase_response import ParaphraseResponse


class TestParaphraseResponse(unittest.TestCase):
    """ParaphraseResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ParaphraseResponse:
        """Test ParaphraseResponse
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ParaphraseResponse`
        """
        model = ParaphraseResponse()
        if include_optional:
            return ParaphraseResponse(
                paraphrased_text = 'This is a rephrased sample text.'
            )
        else:
            return ParaphraseResponse(
                paraphrased_text = 'This is a rephrased sample text.',
        )
        """

    def testParaphraseResponse(self):
        """Test ParaphraseResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()