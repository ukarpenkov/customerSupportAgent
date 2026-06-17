"""Classifier - Determines if query is shipping-related."""

from google.adk.workflow import FunctionNode


def classify_query(state: dict) -> str:
    """Classify user query as shipping-related or unrelated.

    Uses keyword matching for fast, deterministic routing.
    """
    query = state.get("input", "")
    shipping_keywords = [
        "shipping", "track", "tracking", "delivery", "deliver",
        "package", "rate", "rates", "return", "refund", "ship",
        "order", "parcel", "freight", "courier", "express",
        "standard", "overnight", "pickup", "dropoff", "address"
    ]
    query_lower = query.lower()
    for keyword in shipping_keywords:
        if keyword in query_lower:
            return "shipping"
    return "unrelated"


classifier_agent = FunctionNode(
    func=classify_query,
    name="classifier",
)
