from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class Bleurt(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, predicted=None, reference=None):  # noqa: E501
        """Bleurt - a model defined in OpenAPI

        :param predicted: The predicted of this Bleurt.  # noqa: E501
        :type predicted: str
        :param reference: The reference of this Bleurt.  # noqa: E501
        :type reference: str
        """
        self.openapi_types = {
            'predicted': str,
            'reference': str
        }

        self.attribute_map = {
            'predicted': 'predicted',
            'reference': 'reference'
        }

        self._predicted = predicted
        self._reference = reference

    @classmethod
    def from_dict(cls, dikt) -> 'Bleurt':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Bleurt of this Bleurt.  # noqa: E501
        :rtype: Bleurt
        """
        return util.deserialize_model(dikt, cls)

    @property
    def predicted(self) -> str:
        """Gets the predicted of this Bleurt.

        Predicted text.  # noqa: E501

        :return: The predicted of this Bleurt.
        :rtype: str
        """
        return self._predicted

    @predicted.setter
    def predicted(self, predicted: str):
        """Sets the predicted of this Bleurt.

        Predicted text.  # noqa: E501

        :param predicted: The predicted of this Bleurt.
        :type predicted: str
        """
        if predicted is None:
            raise ValueError("Invalid value for `predicted`, must not be `None`")  # noqa: E501

        self._predicted = predicted

    @property
    def reference(self) -> str:
        """Gets the reference of this Bleurt.

        Reference text.  # noqa: E501

        :return: The reference of this Bleurt.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference: str):
        """Sets the reference of this Bleurt.

        Reference text.  # noqa: E501

        :param reference: The reference of this Bleurt.
        :type reference: str
        """
        if reference is None:
            raise ValueError("Invalid value for `reference`, must not be `None`")  # noqa: E501

        self._reference = reference
