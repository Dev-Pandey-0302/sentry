import pytest

from sentry.dynamic_sampling.rules.biases.ignore_health_checks_bias import (
    HEALTH_CHECK_GLOBS,
    IgnoreHealthChecksBias,
)


@pytest.mark.django_db(databases="__all__")
def test_generate_bias_rules_v2(default_project):
    rules = IgnoreHealthChecksBias().generate_rules(project=default_project, base_sample_rate=1.0)
    assert rules == [
        {
            "condition": {
                "inner": [
                    {
                        "name": "event.transaction",
                        "op": "glob",
                        "value": HEALTH_CHECK_GLOBS,
                    }
                ],
                "op": "or",
            },
            "id": 1002,
            "samplingValue": {"type": "sampleRate", "value": 0.2},
            "type": "transaction",
        }
    ]
