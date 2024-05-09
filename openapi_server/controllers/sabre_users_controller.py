import connexion
import evaluate
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.bleurt_model import Bleurt  # noqa: E501
from openapi_server.models.bleurt_score import BleurtScore  # noqa: E501
from openapi_server import util


def compute_bleurt_score(bleurt=None):  # noqa: E501
    """Given a predicted text and a reference text it computes the bleurt score

    The output score is always a number between 0 and (approximately 1). This value indicates how similar the generated text is to the reference texts,  with values closer to 1 representing more similar texts.  # noqa: E501

    :param bleurt: 
    :type bleurt: dict | bytes

    :rtype: Union[BleurtScore, Tuple[BleurtScore, int], Tuple[BleurtScore, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        
        bleurt = Bleurt.from_dict(connexion.request.get_json())  # noqa: E501

    try:
        # Load the BLEURT metric
        evaluateBleurt = evaluate.load("bleurt", module_type="metric")

        # Compute the BLEURT score
        evaluateResults = evaluateBleurt.compute(predictions=[bleurt.predicted], references=[bleurt.reference])
        print("BLEURT score:", evaluateResults)

        return evaluateResults

    except Exception as e:
        print("Error evaluating BLEURT score:", str(e))
        raise  # Reraise the exception for better error handling