import unittest

from flask import json

from bleurt_eval.openapi_server.models.bleurt_model import Bleurt  # noqa: E501
from openapi_server.models.bleurt_score import BleurtScore  # noqa: E501
from openapi_server.test import BaseTestCase


class TestSabreUsersController(BaseTestCase):
    """SabreUsersController integration test stubs"""

    def test_compute_bleurt_score(self):
        """Test case for compute_bleurt_score

        Given a predicted text and a reference text it computes the bleurt score
        """
        bleurt = {"reference":"The sky presents a blue colo because of the dispersion fenomena.","predicted":"The sky is blue."}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/luis-azevedo/bleurt-evalution/1.0.0/bleurt-score',
            method='POST',
            headers=headers,
            data=json.dumps(bleurt),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
