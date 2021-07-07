class BadCallError(ValueError):

    def __init__(self, message=None, documentation_web=None):

        if message is None:
            message = ('Wrong way of invoking this method. Check the online documentation for'
                    'more information.')
            if documentation_web is not None:
                message = message[:-1] + ': {}'.format(documentation_web)

        super().__init__(message)

class NotImplementedError(NotImplementedError):

    def __init__(self, message=None, issues_web=None):

        if message is None:
            if issues_web is not None:
                message = ('It has not been implemeted yet. Write a new issue in'
                '{} asking for it.'.format(issues_web))

        super().__init__(message)


class LibraryNotFound(NotImplementedError):

    def __init__(self, library):

        message = 'The python library {} was not found.'.format(library)

        super().__init__(message)

class InputArgumentError(NotImplementedError):

    def __init__(self, argument, method, documentation_web=None):

        message = ('Invalid value for input argument "{}" in method or class "{}".'
                'Check the online documentation for more information.'.format(argument, method))

        if documentation_web is not None:
            message = message[:-1] + ': {}'.format(documentation_web)

        super().__init__(message)

