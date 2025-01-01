from __future__ import annotations as _annotations

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from dataclasses import dataclass
from typing import Literal

from ..messages import (
    ModelMessage,
    ModelResponse,
)
from ..settings import ModelSettings
from ..tools import ToolDefinition
from . import (
    AgentModel,
    EitherStreamedResponse,
    Model,
)

GrokModelName = Literal['grok-2-vision-1212', 'grok-2-1212', 'grok-2', 'grok-2-latest']


@dataclass(init=False)
class GrokModel(Model):
    client: AsyncGrok
    model_name: GrokModelName
    allow_text_result: bool

    async def request(
        self, messages: list[ModelMessage], model_settings: ModelSettings | None
    ) -> tuple[ModelResponse, Usage]:
        # Implement the request logic here
        pass

    @asynccontextmanager
    async def request_stream(
        self, messages: list[ModelMessage], model_settings: ModelSettings | None
    ) -> AsyncIterator[EitherStreamedResponse]:
        # Implement the streaming request logic here
        pass


@dataclass
class GrokAgentModel(AgentModel):
    client: AsyncGrok
    model_name: GrokModelName
    allow_text_result: bool
    tools: list[ToolDefinition]
