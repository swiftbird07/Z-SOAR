# Tests the IBM QRadar integration

import pytest

from lib.class_helper import Detection, DetectionReport, Rule, ContextProcess, ContextLog, ContextFlow
from integrations.ibm_qradar import zs_provide_new_detections, zs_provide_context_for_detections
import lib.logging_helper as logging_helper
import lib.config_helper as config_helper
import datetime
import uuid

OFFENSE_ID = "1448"  # The ID of an offense that exists in the QRadar test environment


def test_zs_provide_new_detections():
    # Prepare the config
    cfg = config_helper.Config().cfg
    integration_config = cfg["integrations"]["ibm_qradar"]

    detectionArray = zs_provide_new_detections(integration_config, TEST=True)
    assert type(detectionArray) == list, "zs_provide_new_detections() should return a list of Detection objects"
    assert len(detectionArray) > 0, "zs_provide_new_detections() should return a list of Detection objects"
    for detection in detectionArray:
        assert type(detection) == Detection, "zs_provide_new_detections() found an invalid Detection object in the list"


def test_zs_provide_context_for_detections():
    # Prepare the config
    cfg = config_helper.Config().cfg
    integration_config = cfg["integrations"]["ibm_qradar"]

    # Prepare a DetectionReport object
    rule = Rule("123", "Some Rule", 0)

    ruleList = []
    ruleList.append(rule)
    detection = Detection("789", "A QRadar Detection", ruleList, datetime.datetime.now(), uuid=OFFENSE_ID)

    detectionList = []
    detectionList.append(detection)
    detection_report = DetectionReport(detectionList)
    assert (
        detection_report != None
    ), "DetectionReport class could not be initialized"  # Sanity check - should be already tested by test_zsoar_lib.py -> test_class_helper()

    # Get the context
    detectionArray = zs_provide_context_for_detections(
        detection_report, ContextFlow, TEST=True, search_type="offense", search_value=OFFENSE_ID
    )
    assert type(detectionArray) == list, "zs_provide_context_for_detections() should return a list of ContextFlow objects"
    assert len(detectionArray) > 0, "zs_provide_context_for_detections() should return a list of ContextFlow objects"
    for detection in detectionArray:
        assert (
            type(detection) == ContextFlow
        ), "zs_provide_context_for_detections() found an invalid ContextFlow object in the list"

    detectionArray = zs_provide_context_for_detections(
        detection_report, ContextLog, TEST=True, search_type="offense", search_value=OFFENSE_ID
    )
    assert type(detectionArray) == list, "zs_provide_context_for_detections() should return a list of ContextLog objects"
    assert len(detectionArray) > 0, "zs_provide_context_for_detections() should return a list of ContextLog objects"
    for detection in detectionArray:
        assert type(detection) == ContextLog, "zs_provide_context_for_detections() found an invalid ContextLog object in the list"