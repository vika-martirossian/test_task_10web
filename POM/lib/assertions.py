# pip  install PyHamcrest

from hamcrest import core, library
from hamcrest._version import version

__version__ = version
__author__ = "Chris Rose"
__copyright__ = "Copyright 2020 hamcrest.org"
__license__ = "BSD, see License.txt"

__all__ = []

__all__.extend(core.__all__)
__all__.extend(library.__all__)
import warnings
from typing import Optional, TypeVar, cast

from hamcrest.core.matcher import Matcher
from hamcrest.core.string_description import StringDescription

# unittest integration; hide these frames from tracebacks
__unittest = True
# py.test integration; hide these frames from tracebacks
__tracebackhide__ = True

T = TypeVar("T")


def assert_that(actual_or_assertion, matcher=None, reason=""):
    if isinstance(matcher, Matcher):
        _assert_match(actual=actual_or_assertion, matcher=matcher, reason=reason)
    else:
        if isinstance(actual_or_assertion, Matcher):
            warnings.warn("arg1 should be boolean, but was {}".format(type(actual_or_assertion)))
        _assert_bool(assertion=cast(bool, actual_or_assertion), reason=cast(str, matcher))


def _assert_match(actual: T, matcher: Matcher[T], reason: str) -> None:
    if not matcher.matches(actual):
        description = StringDescription()
        description.append_text(reason).append_text("\nExpected: ").append_description_of(
            matcher
        ).append_text("\n     but: ")
        matcher.describe_mismatch(actual, description)
        description.append_text("\n")
        raise AssertionError(description)


def _assert_bool(assertion: bool, reason: Optional[str] = None) -> None:
    if not assertion:
        if not reason:
            reason = "Assertion failed"
        raise AssertionError(reason)
