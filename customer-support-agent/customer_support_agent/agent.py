"""Customer Support Agent - Graph workflow for shipping company support."""

from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.workflow import Workflow, FunctionNode, Edge
from google.adk.workflow._graph import Graph

from customer_support_agent.classifier import classifier_agent
from customer_support_agent.shipping_faq import shipping_faq_agent


def decline_response(state: dict) -> str:
    """Generate a polite decline response for unrelated queries."""
    return (
        "Thank you for your message. I'm here to help with shipping-related "
        "questions only, including:\n\n"
        "- Shipping rates and pricing\n"
        "- Package tracking\n"
        "- Delivery information\n"
        "- Returns and refunds\n\n"
        "For other inquiries, please visit our website or contact our general "
        "support line. Is there anything about shipping I can help you with?"
    )


decline_node = FunctionNode(func=decline_response, name="decline")


workflow = Workflow(
    name="customer_support_workflow",
    description="Graph workflow for customer support routing",
    graph=Graph(
        edges=[
            Edge(from_node=classifier_agent, to_node=shipping_faq_agent, route="shipping"),
            Edge(from_node=classifier_agent, to_node=decline_node, route="unrelated"),
        ],
    ),
)


root_agent = Agent(
    name="customer_support_agent",
    model=LiteLlm(model="deepseek/deepseek-chat"),
    description="Customer support representative for a shipping company",
    instruction="""You are a customer support agent for a shipping company.

Your workflow:
1. First, classify the user's query to determine if it's related to shipping
2. If it's about shipping (rates, tracking, delivery, returns), route to the FAQ agent
3. If it's unrelated, politely decline to answer

Always be helpful and professional.""",
)


def main():
    """Entry point for running the agent."""
    from google.adk.runners import Runner
    from google.adk.sessions import InMemorySessionService

    session_service = InMemorySessionService()
    runner = Runner(
        agent=root_agent,
        session_service=session_service,
    )
    runner.run()


if __name__ == "__main__":
    main()
