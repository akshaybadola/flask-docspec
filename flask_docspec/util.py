from typing import Dict, Any, Callable, Optional


def dget(obj, *args):
    if args:
        return dget(obj.get(args[0]), *args[1:])
    else:
        return obj


def recurse_dict(jdict: Dict[str, Any],
                 pred: Callable[[str, Any], bool],
                 repl: Callable[[str, str], str],
                 repl_only: bool = False) -> Dict[str, Any]:
    """Recurse over a :class:`dict` and perform replacement.

    This function replaces the values of the dictionary in place. Used to
    fix the generated schema :class:`dict`.

    Args:
        jdict: A dictionary
        pred: Predicate to check when to perform replacement
        repl: Function which performs the replacement

    Returns:
        A modified dictionary

    """
    if not (isinstance(jdict, dict) or isinstance(jdict, list)):
        return jdict
    if isinstance(jdict, dict):
        for k, v in jdict.items():
            if pred(k, v):
                jdict[k] = repl(k, v)
                if repl_only:
                    continue
            if isinstance(v, dict):
                jdict[k] = recurse_dict(v, pred, repl, repl_only)
            if isinstance(v, list):
                for i, item in enumerate(v):
                    v[i] = recurse_dict(item, pred, repl, repl_only)
    elif isinstance(jdict, list):
        for i, item in enumerate(jdict):
            jdict[i] = recurse_dict(item, pred, repl, repl_only)
    return jdict


def pop_if(jdict: Dict[str, Any], pred: Callable[[str, Any], bool]) -> Dict[str, Any]:
    """Pop a (key, value) pair based on predicate `pred`.

    Args:
        jdict: A dictionary
        pred: According to which the value is popped

    Returns:
        A :class:`dict` of popped values.

    """
    to_pop = []
    popped = {}
    for k, v in jdict.items():
        if pred(k, v):
            to_pop.append(k)
        if isinstance(v, dict):
            popped.update(pop_if(v, pred))
    for p in to_pop:
        popped.update(jdict.pop(p))
    return popped


def exec_and_return(exec_str: str,
                    modules: Optional[Dict[str, Any]] = None) -> Any:
    """Execute the exec_str with :meth:`exec` and return the value

    Args:
        exec_str: The string to execute

    Returns:
        The value in the `exec_str`

    """
    ldict: Dict[str, Any] = {}
    if modules is not None:
        exec("testvar = " + exec_str, {**modules, **globals()}, ldict)
    else:
        exec("testvar = " + exec_str, globals(), ldict)
    retval = ldict['testvar']
    return retval
