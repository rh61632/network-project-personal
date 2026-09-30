LAT_MIN, LAT_MAX = 20.5, 26.7
LON_MIN, LON_MAX = 88.0, 92.7

OPERATOR_MAP = {
    1: "Grameenphone",
    2: "Robi",
    3: "Banglalink",
    4: "Teletalk"
}

SCHEMA_COLUMNS = [
    "radio", "mcc", "net", "area", "cell", "unit", "lon", "lat", "range", "samples", "changeable", "created", "updated", "averageSignal"
]
OPERATOR_COLOR = {
    "Grameenphone" : "#0090ff",
    "Robi" : "#e60000",
    "Banglalink" : "#ff7a00",
    "Teletalk" : "#00873d"
}
