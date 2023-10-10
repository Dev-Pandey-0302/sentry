from drf_spectacular.utils import OpenApiExample


class MetricAlertExamples:
    LIST_METRIC_ALERT_RULES = [
        OpenApiExample(
            "List metric alert rules for an organization",
            value=[
                {
                    "id": "7",
                    "name": "Counting Bad Request and Unauthorized Errors in Prod",
                    "organizationId": "237655244234",
                    "queryType": 0,
                    "dataset": "events",
                    "query": "tags[http.status_code]:[400, 401]",
                    "aggregate": "count()",
                    "thresholdType": 0,
                    "resolveThreshold": None,
                    "timeWindow": "1440",
                    "environment": "prod",
                    "triggers": [
                        {
                            "id": "394289",
                            "alertRuleId": "17723",
                            "label": "critical",
                            "thresholdType": 0,
                            "alertThreshold": 100,
                            "resolveThreshold": None,
                            "dateCreated": "2023-09-25T22:15:26.375126Z",
                            "actions": [
                                {
                                    "id": "394280",
                                    "alertRuleTriggerId": "92481",
                                    "type": "slack",
                                    "targetType": "specific",
                                    "targetIdentifier": "30489048931789",
                                    "inputChannelId": "#my-channel",
                                    "integrationId": "8753467",
                                    "sentryAppId": None,
                                    "dateCreated": "2023-09-25T22:15:26.375126Z",
                                }
                            ],
                        },
                    ],
                    "projects": ["super-cool-project"],
                    "owner": "user:53256",
                    "originalAlertRuleId": None,
                    "comparisonDelta": None,
                    "dateModified": "2023-09-25T22:15:26.375126Z",
                    "dateCreated": "2023-09-25T22:15:26.375126Z",
                    "createdBy": {"id": 983948, "name": "John Doe", "email": "john.doe@sentry.io"},
                }
            ],
            status_codes=["200"],
            response_only=True,
        )
    ]

    CREATE_METRIC_ALERT_RULE = [
        OpenApiExample(
            "Create a metric alert rule for an organization",
            value={
                "id": "177104",
                "name": "Apdex % Check",
                "organizationId": "4505676595200000",
                "queryType": 2,
                "dataset": "metrics",
                "query": "",
                "aggregate": "percentage(sessions_crashed, sessions) AS _crash_rate_alert_aggregate",
                "thresholdType": 0,
                "resolveThreshold": 80.0,
                "timeWindow": "120",
                "environment": None,
                "triggers": [
                    {
                        "id": "293990",
                        "alertRuleId": "177104",
                        "label": "critical",
                        "thresholdType": 0,
                        "alertThreshold": 75,
                        "resolveThreshold": 80.0,
                        "dateCreated": "2023-09-25T22:01:28.673305Z",
                        "actions": [
                            {
                                "id": "281887",
                                "alertRuleTriggerId": "293990",
                                "type": "email",
                                "targetType": "team",
                                "targetIdentifier": "2378589792734981",
                                "inputChannelId": None,
                                "integrationId": None,
                                "sentryAppId": None,
                                "dateCreated": "2023-09-25T22:01:28.680793Z",
                            }
                        ],
                    },
                    {
                        "id": "492849",
                        "alertRuleId": "482923",
                        "label": "warning",
                        "thresholdType": 1,
                        "alertThreshold": 50,
                        "resolveThreshold": 80,
                        "dateCreated": "2023-09-25T22:01:28.673305Z",
                        "actions": [],
                    },
                ],
                "projects": ["our-project"],
                "owner": "team:4505676595200000",
                "originalAlertRuleId": None,
                "comparisonDelta": 10080,
                "dateModified": "2023-09-25T22:01:28.637506Z",
                "dateCreated": "2023-09-25T22:01:28.637514Z",
                "createdBy": {
                    "id": 2837708,
                    "name": "Jane Doe",
                    "email": "jane.doe@sentry.io",
                },
            },
            status_codes=["201"],
            response_only=True,
        )
    ]