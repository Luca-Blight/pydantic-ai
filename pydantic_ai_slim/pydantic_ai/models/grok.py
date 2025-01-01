from __future__ import annotations as _annotations

from collections.abc import AsyncIterator
from dataclasses import dataclass
from typing import EitherStreamedResponse, Literal

from asynccontextmanager import asynccontextmanager
from groq import AsyncGrok

from ..messages import (
    ModelMessage,
)
from ..result import Usage
from ..settings import ModelSettings
from . import (
    AgentModel,
    Model,
)

GrokModelName = Literal['grok-2-vision-1212', 'grok-2-1212', 'grok-2', 'grok-2-latest']


@dataclass(init=False)
class GrokModel(Model):
    client: AsyncGrok
    model_name: GrokModelName
    allow_text_result: bool

    def __init__(self, model_name: GrokModelName, api_key: str | None = None):
        # Initialize the GrokModel
        self.model_name = model_name
        self.client = AsyncGrok(api_key=api_key)

    async def request(
        self, messages: list[ModelMessage], model_settings: ModelSettings | None
    ) -> tuple[ModelResponse, Usage]:
        # Implement the request logic here
        # Example return statement
        return ModelResponse(), Usage()

    @asynccontextmanager
    async def request_stream(
        self, messages: list[ModelMessage], model_settings: ModelSettings | None
    ) -> AsyncIterator[EitherStreamedResponse]:
        # Implement the streaming request logic here
        yield EitherStreamedResponse()


@dataclass
class GrokAgentModel(AgentModel):
    client: AsyncGrok
    model_name: GrokModelName
    allow_text_result: bool

    def __init__(self, client: AsyncGrok, model_name: GrokModelName, allow_text_result: bool):
        self.client = client
        self.model_name = model_name
        self.allow_text_result = allow_text_result

    async def request(
        self, messages: list[ModelMessage], model_settings: ModelSettings | None
    ) -> tuple[ModelResponse, Usage]:
        # Implement the request logic here
        return ModelResponse(), Usage()

    @asynccontextmanager
    async def request_stream(
        self, messages: list[ModelMessage], model_settings: ModelSettings | None
    ) -> AsyncIterator[EitherStreamedResponse]:
        # Implement the streaming request logic here
        yield EitherStreamedResponse()
