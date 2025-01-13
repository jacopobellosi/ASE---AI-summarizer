from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class ParaphrasePostRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, text=None, style=None):  # noqa: E501
        """ParaphrasePostRequest - a model defined in OpenAPI

        :param text: The text of this ParaphrasePostRequest.  # noqa: E501
        :type text: str
        :param style: The style of this ParaphrasePostRequest.  # noqa: E501
        :type style: str
        """
        self.openapi_types = {
            'text': str,
            'style': str
        }

        self.attribute_map = {
            'text': 'text',
            'style': 'style'
        }

        self._text = text
        self._style = style

    @classmethod
    def from_dict(cls, dikt) -> 'ParaphrasePostRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _paraphrase_post_request of this ParaphrasePostRequest.  # noqa: E501
        :rtype: ParaphrasePostRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def text(self) -> str:
        """Gets the text of this ParaphrasePostRequest.


        :return: The text of this ParaphrasePostRequest.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text: str):
        """Sets the text of this ParaphrasePostRequest.


        :param text: The text of this ParaphrasePostRequest.
        :type text: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    @property
    def style(self) -> str:
        """Gets the style of this ParaphrasePostRequest.


        :return: The style of this ParaphrasePostRequest.
        :rtype: str
        """
        return self._style

    @style.setter
    def style(self, style: str):
        """Sets the style of this ParaphrasePostRequest.


        :param style: The style of this ParaphrasePostRequest.
        :type style: str
        """

        self._style = style
