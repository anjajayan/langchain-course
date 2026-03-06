from typing import List

from pydantic import BaseModel, Field


class Source(BaseModel):
    """Schema for the source used by the agent"""

    url: str = Field(description="The URL of the source")


class AgentResponse(BaseModel):
    """Schema for the agent response with answer and source"""

    answer: str = Field(description="The agent's answer to a query")
    sources: List[Source] = Field(
        description="The list of sources used to generate the answer",
        default_factory=List,
    )
