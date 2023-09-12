"""`eds.myocardial_infarction` pipeline"""
from typing import Generator

from spacy.tokens import Doc, Span

from edsnlp.pipelines.ner.disorders.base import DisorderMatcher

from .patterns import default_patterns


class MyocardialInfarction(DisorderMatcher):
    def __init__(self, nlp, name, patterns):

        self.nlp = nlp
        if patterns is None:
            patterns = default_patterns

        super().__init__(
            nlp=nlp,
            name=name,
            label_name="myocardial_infarction",
            patterns=patterns,
        )

    def postprocess(self, doc: Doc, spans: Generator[Span, None, None]):
        for span in spans:

            if (
                span._.source == "with_localization"
                and "heart_localized" not in span._.assigned
            ):
                continue

            yield span