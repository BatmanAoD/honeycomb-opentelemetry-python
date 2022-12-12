from honeycomb.opentelemetry.options import HoneycombOptions
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import (
    OTLPSpanExporter
)


def create_tracer_provider(options: HoneycombOptions, resource: Resource):
    trace_provider = TracerProvider(resource=resource)
    trace_provider.add_span_processor(
        BatchSpanProcessor(
            OTLPSpanExporter(
                endpoint=options.endpoint,
                credentials=options.get_trace_endpoint_credentials(),
                headers=options.get_trace_headers()
            )
        )
    )
    return trace_provider