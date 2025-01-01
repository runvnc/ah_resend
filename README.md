# Resend Email Provider for MindRoot

This plugin provides integration with Resend.com email service for MindRoot.

## Installation

```bash
pip install -e .
```

## Configuration

Set the following environment variables:

```bash
RESEND_API_KEY=your_api_key_here
SMTP_FROM="MindRoot <noreply@yourdomain.com>"  # Optional, defaults to MindRoot <noreply@mindroot.ai>
```

## Usage

The plugin provides a `send_email` service that can be used by other plugins:

```python
from lib.providers.services import service_manager

await service_manager.send_email({
    "to": "user@example.com",
    "subject": "Test Email",
    "body": "<h1>Hello World</h1>",
    "html": True
})
```

## Features

- HTML and plain text email support
- Modern API with excellent deliverability
- Simple configuration
- Async implementation
- Error handling and logging

## Development

To run tests:

```bash
python -m pytest tests/
```
