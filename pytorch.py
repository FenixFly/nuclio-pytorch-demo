

def do(context, event):
    context.logger.info('This is an unstructured log')

    return context.Response(body='Hello, from nuclio :]',
                            headers={},
                            content_type='text/plain',
                            status_code=200)