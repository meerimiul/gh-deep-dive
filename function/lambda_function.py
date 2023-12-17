from github import Github

def lambda_handler(event, context):
    """Lambda function wrapper
    Args:
        event: trigger event dict
        context: lambda methods and properties
    Returns:
        string: greeting response
    """
    # print('Starting functions\n---------------------------------------------'
    print('Starting functions\n---------------------------------------------')

    if event["input"] == "Hello":

        return "World"

    if event["input"] == "Hola":

        return "Mundo"

    if event["input"] == "Bonjour":

        return "le Monde"

    if event["input"] == "Привет":

        return "Мир"

    else:

        raise