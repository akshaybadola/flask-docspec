from .openapi import openapi_spec, fix_redundancies, fix_yaml_references, update_security_schemes


def _init(modules):
    from . import parser
    parser.global_modules.update(modules)
    parser.global_modules.update({x.__name__: x for x in modules.values()})


__all__ = ["openapi_spec", "fix_redundancies", "fix_yaml_references", "update_security_schemes"]
