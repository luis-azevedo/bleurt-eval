from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class BleurtScore(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, score=None):  # noqa: E501
        """BleurtScore - a model defined in OpenAPI

        :param score: The score of this BleurtScore.  # noqa: E501
        :type score: float
        """
        self.openapi_types = {
            'score': float
        }

        self.attribute_map = {
            'score': 'score'
        }

        self._score = score

    @classmethod
    def from_dict(cls, dikt) -> 'BleurtScore':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BleurtScore of this BleurtScore.  # noqa: E501
        :rtype: BleurtScore
        """
        return util.deserialize_model(dikt, cls)

    @property
    def score(self) -> float:
        """Gets the score of this BleurtScore.

        Bleurt score output.  # noqa: E501

        :return: The score of this BleurtScore.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score: float):
        """Sets the score of this BleurtScore.

        Bleurt score output.  # noqa: E501

        :param score: The score of this BleurtScore.
        :type score: float
        """

        self._score = score