#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CAVEAT UTILITOR
#
# This file was automatically generated by TatSu.
#
#    https://pypi.python.org/pypi/tatsu/
#
# Any changes you make to it will be overwritten the next time
# the file is generated.


from __future__ import print_function, division, absolute_import, unicode_literals

import sys

from tatsu.buffering import Buffer
from tatsu.parsing import Parser
from tatsu.parsing import tatsumasu, leftrec, nomemo
from tatsu.parsing import leftrec, nomemo  # noqa
from tatsu.util import re, generic_main  # noqa


KEYWORDS = {}  # type: ignore


class UnknownBuffer(Buffer):
    def __init__(
        self,
        text,
        whitespace=re.compile(" "),
        nameguard=None,
        comments_re=None,
        eol_comments_re=None,
        ignorecase=None,
        namechars="",
        **kwargs
    ):
        super(UnknownBuffer, self).__init__(
            text,
            whitespace=whitespace,
            nameguard=nameguard,
            comments_re=comments_re,
            eol_comments_re=eol_comments_re,
            ignorecase=ignorecase,
            namechars=namechars,
            **kwargs
        )


class UnknownParser(Parser):
    def __init__(
        self,
        whitespace=re.compile(" "),
        nameguard=None,
        comments_re=None,
        eol_comments_re=None,
        ignorecase=None,
        left_recursion=True,
        parseinfo=True,
        keywords=None,
        namechars="",
        buffer_class=UnknownBuffer,
        **kwargs
    ):
        if keywords is None:
            keywords = KEYWORDS
        super(UnknownParser, self).__init__(
            whitespace=whitespace,
            nameguard=nameguard,
            comments_re=comments_re,
            eol_comments_re=eol_comments_re,
            ignorecase=ignorecase,
            left_recursion=left_recursion,
            parseinfo=parseinfo,
            keywords=keywords,
            namechars=namechars,
            buffer_class=buffer_class,
            **kwargs
        )

    @tatsumasu()
    def _start_(self):  # noqa
        self._statements_()
        self._check_eof()

    @tatsumasu()
    def _statements_(self):  # noqa
        def block0():
            self._statement_()

        self._positive_closure(block0)

    @tatsumasu()
    def _statement_(self):  # noqa
        with self._choice():
            with self._option():
                self._simple_stmt_()
            with self._option():
                self._compound_stmt_()
            self._error("no available options")

    @tatsumasu()
    def _simple_stmt_(self):  # noqa
        self._small_stmt_()

        def block0():
            self._token(";")
            self._small_stmt_()

        self._closure(block0)
        self._NEWLINE_()

    @tatsumasu()
    def _small_stmt_(self):  # noqa
        with self._choice():
            with self._option():
                self._return_stmt_()
            with self._option():
                self._import_stmt_()
            with self._option():
                self._token("pass")
            with self._option():
                self._assignment_()
            with self._option():
                self._expression_()
            self._error("no available options")

    @tatsumasu()
    def _compound_stmt_(self):  # noqa
        with self._choice():
            with self._option():
                self._if_stmt_()
            with self._option():
                self._while_stmt_()
            with self._option():
                self._with_stmt_()
            with self._option():
                self._function_def_()
            with self._option():
                self._class_def_()
            self._error("no available options")

    @tatsumasu()
    def _assignment_(self):  # noqa
        self._target_()
        self._token("=")
        self._expression_()

    @tatsumasu()
    def _import_stmt_(self):  # noqa
        with self._choice():
            with self._option():
                self._token("import")
                self._names_()
            with self._option():
                self._token("from")
                self._NAME_()
                self._token("import")
                with self._group():
                    with self._choice():
                        with self._option():
                            self._token("*")
                        with self._option():
                            self._names_()
                        self._error("no available options")
            self._error("no available options")

    @tatsumasu()
    def _names_(self):  # noqa
        with self._choice():
            with self._option():
                self._NAME_()
                self._token(",")
                self._names_()
            with self._option():
                self._NAME_()
            self._error("no available options")

    @tatsumasu()
    def _if_stmt_(self):  # noqa
        self._token("if")
        self._full_expression_()
        self._token(":")
        self._block_()

        def block0():
            self._elif_block_()

        self._closure(block0)
        with self._optional():
            self._else_block_()

    @tatsumasu()
    def _elif_block_(self):  # noqa
        self._token("elif")
        self._full_expression_()
        self._token(":")
        self._block_()

    @tatsumasu()
    def _else_block_(self):  # noqa
        self._token("else")
        self._token(":")
        self._block_()

    @tatsumasu()
    def _while_stmt_(self):  # noqa
        self._token("while")
        self._full_expression_()
        self._token(":")
        self._block_()
        with self._optional():
            self._else_block_()

    @tatsumasu()
    def _with_stmt_(self):  # noqa
        self._token("with")
        self._expression_()
        with self._optional():
            self._token("as")
            self._target_()
        self._token(":")
        self._block_()

    @tatsumasu()
    def _return_stmt_(self):  # noqa
        self._token("return")
        with self._optional():
            self._expressions_()

    @tatsumasu()
    def _function_def_(self):  # noqa
        with self._optional():
            self._decorators_()
        self._token("def")
        self._NAME_()
        self._token("(")
        with self._optional():
            self._parameters_()
        self._token(")")
        self._token(":")
        self._block_()

    @tatsumasu()
    def _parameters_(self):  # noqa
        with self._choice():
            with self._option():
                self._kwparams_()
            with self._option():
                self._param_()
                with self._optional():
                    self._token(",")
                    with self._optional():
                        self._parameters_()
            self._error("no available options")

    @tatsumasu()
    def _kwparams_(self):  # noqa
        self._kwparam_()
        with self._optional():
            self._token(",")
            with self._optional():
                self._kwparams_()

    @tatsumasu()
    def _kwparam_(self):  # noqa
        with self._choice():
            with self._option():
                self._NAME_()
                self._token("=")
                self._expression_()
            with self._option():
                self._token("**")
                self._NAME_()
            self._error("no available options")

    @tatsumasu()
    def _param_(self):  # noqa
        with self._choice():
            with self._option():
                self._NAME_()
            with self._option():
                self._token("*")
                self._NAME_()
            self._error("no available options")

    @tatsumasu()
    def _decorators_(self):  # noqa
        def block0():
            self._token("@")
            self._factor_()
            self._NEWLINE_()

        self._positive_closure(block0)

    @tatsumasu()
    def _class_def_(self):  # noqa
        with self._optional():
            self._decorators_()
        self._token("class")
        self._NAME_()
        with self._optional():
            self._token("(")
            self._full_expressions_()
            self._token(")")
        self._token(":")
        self._block_()

    @tatsumasu()
    def _block_(self):  # noqa
        with self._choice():
            with self._option():
                self._simple_stmt_()
            with self._option():
                self._NEWLINE_()
                self._INDENT_()
                self._statements_()
                self._DEDENT_()
            self._error("no available options")

    @tatsumasu()
    def _full_expressions_(self):  # noqa
        self._full_expression_()

        def block0():
            self._token(",")
            self._full_expression_()

        self._closure(block0)
        with self._optional():
            self._token(",")

    @tatsumasu()
    def _full_expression_(self):  # noqa
        with self._choice():
            with self._option():
                self._NAME_()
                self._token(":=")
                self._disjunction_()
            with self._option():
                self._disjunction_()
            self._error("no available options")

    @tatsumasu()
    def _disjunction_(self):  # noqa
        self._conjunction_()

        def block0():
            self._token("or")
            self._conjunction_()

        self._closure(block0)

    @tatsumasu()
    def _conjunction_(self):  # noqa
        self._comparison_()

        def block0():
            self._token("and")
            self._comparison_()

        self._closure(block0)

    @tatsumasu()
    def _comparison_(self):  # noqa
        def block0():
            self._token("not")

        self._closure(block0)
        self._bitwise_or_()

        def block1():
            self._compare_op_()
            self._bitwise_or_()

        self._closure(block1)

    @tatsumasu()
    def _compare_op_(self):  # noqa
        with self._choice():
            with self._option():
                self._token("<")
            with self._option():
                self._token("<=")
            with self._option():
                self._token("==")
            with self._option():
                self._token(">=")
            with self._option():
                self._token(">")
            with self._option():
                self._token("!=")
            with self._option():
                self._token("in")
            with self._option():
                self._token("not in")
            self._error("no available options")

    @tatsumasu()
    def _bitwise_or_(self):  # noqa
        self._bitwise_and_()

        def block0():
            self._token("|")
            self._bitwise_and_()

        self._closure(block0)

    @tatsumasu()
    def _bitwise_and_(self):  # noqa
        self._expression_()

        def block0():
            self._token("&")
            self._expression_()

        self._closure(block0)

    @tatsumasu()
    def _expressions_(self):  # noqa
        self._expression_()

        def block0():
            self._token(",")
            self._expression_()

        self._closure(block0)
        with self._optional():
            self._token(",")

    @tatsumasu()
    def _expression_(self):  # noqa
        self._term_()

        def block0():
            with self._choice():
                with self._option():
                    self._token("+")
                    self._term_()
                with self._option():
                    self._token("-")
                    self._term_()
                self._error("no available options")

        self._closure(block0)

    @tatsumasu()
    def _term_(self):  # noqa
        self._factor_()

        def block0():
            with self._choice():
                with self._option():
                    self._token("*")
                    self._factor_()
                with self._option():
                    self._token("/")
                    self._factor_()
                self._error("no available options")

        self._closure(block0)

    @tatsumasu()
    def _factor_(self):  # noqa
        self._primary_()

        def block0():
            with self._choice():
                with self._option():
                    self._token(".")
                    self._NAME_()
                with self._option():
                    self._token("[")
                    self._expression_()
                    self._token("]")
                with self._option():
                    self._token("(")
                    with self._optional():
                        self._arguments_()
                        with self._optional():
                            self._token(",")
                    self._token(")")
                self._error("no available options")

        self._closure(block0)

    @tatsumasu()
    def _primary_(self):  # noqa
        with self._choice():
            with self._option():
                self._list_()
            with self._option():
                self._tuple_()
            with self._option():
                self._group_()
            with self._option():
                self._NAME_()
            with self._option():
                self._STRING_()
            with self._option():
                self._NUMBER_()
            self._error("no available options")

    @tatsumasu()
    def _list_(self):  # noqa
        self._token("[")
        with self._optional():
            self._full_expressions_()
        self._token("]")

    @tatsumasu()
    def _tuple_(self):  # noqa
        self._token("(")
        with self._optional():
            self._full_expression_()
            self._token(",")
            with self._optional():
                self._full_expressions_()
        self._token(")")

    @tatsumasu()
    def _group_(self):  # noqa
        self._token("(")
        self._full_expression_()
        self._token(")")

    @tatsumasu()
    def _arguments_(self):  # noqa
        with self._choice():
            with self._option():
                self._kwargs_()
            with self._option():
                self._posarg_()
                with self._optional():
                    self._token(",")
                    self._arguments_()
            self._error("no available options")

    @tatsumasu()
    def _kwargs_(self):  # noqa
        self._kwarg_()

        def block0():
            self._token(",")
            self._kwarg_()

        self._closure(block0)

    @tatsumasu()
    def _posarg_(self):  # noqa
        with self._choice():
            with self._option():
                self._full_expression_()
            with self._option():
                self._token("*")
                self._disjunction_()
            self._error("no available options")

    @tatsumasu()
    def _kwarg_(self):  # noqa
        with self._choice():
            with self._option():
                self._NAME_()
                self._token("=")
                self._disjunction_()
            with self._option():
                self._token("**")
                self._disjunction_()
            self._error("no available options")

    @tatsumasu()
    def _target_(self):  # noqa
        self._NAME_()

    @tatsumasu()
    def _STRING_(self):  # noqa
        self._str_()

    @tatsumasu()
    def _NUMBER_(self):  # noqa
        self._number_()

    @tatsumasu()
    def _NEWLINE_(self):  # noqa
        self._newline_()

    @tatsumasu()
    def _str_(self):  # noqa
        with self._choice():
            with self._option():
                self._STRING_LITERAL_()
            with self._option():
                self._BYTES_LITERAL_()
            self._error("no available options")

    @tatsumasu()
    def _number_(self):  # noqa
        with self._choice():
            with self._option():
                self._integer_()
            with self._option():
                self._float_number_()
            with self._option():
                self._IMAG_NUMBER_()
            self._error("no available options")

    @tatsumasu()
    def _integer_(self):  # noqa
        with self._choice():
            with self._option():
                self._decimal_integer_()
            with self._option():
                self._OCT_INTEGER_()
            with self._option():
                self._HEX_INTEGER_()
            with self._option():
                self._BIN_INTEGER_()
            self._error("no available options")

    @tatsumasu()
    def _newline_(self):  # noqa
        with self._group():
            with self._choice():
                with self._option():
                    self._SPACES_()
                with self._option():
                    with self._group():
                        with self._optional():
                            self._token("\\r")
                        self._pattern("[\\n\\r\\f]")
                    with self._optional():
                        self._SPACES_()
                self._error("no available options")

    @tatsumasu()
    def _NAME_(self):  # noqa
        self._ID_START_()

        def block0():
            self._ID_CONTINUE_()

        self._closure(block0)

    @tatsumasu()
    def _STRING_LITERAL_(self):  # noqa
        self._pattern("[uU]?[rR]?")
        with self._group():
            with self._choice():
                with self._option():
                    self._SHORT_STRING_()
                with self._option():
                    self._LONG_STRING_()
                self._error("no available options")

    @tatsumasu()
    def _BYTES_LITERAL_(self):  # noqa
        self._pattern("[bB][rR]?")
        with self._group():
            with self._choice():
                with self._option():
                    self._SHORT_BYTES_()
                with self._option():
                    self._LONG_BYTES_()
                self._error("no available options")

    @tatsumasu()
    def _decimal_integer_(self):  # noqa
        with self._choice():
            with self._option():
                self._NON_ZERO_DIGIT_()

                def block0():
                    self._DIGIT_()

                self._closure(block0)
            with self._option():

                def block1():
                    self._token("0")

                self._positive_closure(block1)
            self._error("no available options")

    @tatsumasu()
    def _OCT_INTEGER_(self):  # noqa
        self._token("0")
        self._pattern("[oO]")

        def block0():
            self._OCT_DIGIT_()

        self._positive_closure(block0)

    @tatsumasu()
    def _HEX_INTEGER_(self):  # noqa
        self._token("0")
        self._pattern("[xX]")

        def block0():
            self._HEX_DIGIT_()

        self._positive_closure(block0)

    @tatsumasu()
    def _BIN_INTEGER_(self):  # noqa
        self._token("0")
        self._pattern("[bB]")

        def block0():
            self._BIN_DIGIT_()

        self._positive_closure(block0)

    @tatsumasu()
    def _float_number_(self):  # noqa
        with self._choice():
            with self._option():
                self._POINT_FLOAT_()
            with self._option():
                self._EXPONENT_FLOAT_()
            self._error("no available options")

    @tatsumasu()
    def _IMAG_NUMBER_(self):  # noqa
        with self._group():
            with self._choice():
                with self._option():
                    self._float_number_()
                with self._option():
                    self._INT_PART_()
                self._error("no available options")
        self._pattern("[jJ]")

    @tatsumasu()
    def _skip__(self):  # noqa
        with self._group():
            with self._choice():
                with self._option():
                    self._SPACES_()
                with self._option():
                    self._COMMENT_()
                with self._option():
                    self._LINE_JOINING_()
                self._error("no available options")

    @tatsumasu()
    def _unknown_char_(self):  # noqa
        self._pattern("\\w+|\\S+")

    @tatsumasu()
    def _SHORT_STRING_(self):  # noqa
        self._token("\\'")

        def block0():
            with self._choice():
                with self._option():
                    self._STRING_ESCAPE_SEQ_()
                with self._option():
                    self._pattern("[^\\\\\\r\\n\\f']")
                self._error("no available options")

        self._closure(block0)
        self._pattern("[\\'\"]")

        def block2():
            with self._choice():
                with self._option():
                    self._STRING_ESCAPE_SEQ_()
                with self._option():
                    self._pattern('[^\\\\\\r\\n\\f"]')
                self._error("no available options")

        self._closure(block2)
        self._token('"')

    @tatsumasu()
    def _LONG_STRING_(self):  # noqa
        with self._choice():
            with self._option():
                self._token("\\'\\'\\'")
                with self._optional():
                    self._LONG_STRING_ITEM_()
                self._token("\\'\\'\\'")
            with self._option():
                self._token('"""')
                with self._optional():
                    self._LONG_STRING_ITEM_()
                self._token('"""')
            self._error("no available options")

    @tatsumasu()
    def _LONG_STRING_ITEM_(self):  # noqa
        with self._choice():
            with self._option():
                self._LONG_STRING_CHAR_()
            with self._option():
                self._STRING_ESCAPE_SEQ_()
            self._error("no available options")

    @tatsumasu()
    def _LONG_STRING_CHAR_(self):  # noqa
        with self._ifnot():
            self._token("\\\\")
        self._pattern(".")

    @tatsumasu()
    def _STRING_ESCAPE_SEQ_(self):  # noqa
        self._token("\\\\")
        self._pattern("\\w+|\\S+")

    @tatsumasu()
    def _NON_ZERO_DIGIT_(self):  # noqa
        self._pattern("[1-9]")

    @tatsumasu()
    def _DIGIT_(self):  # noqa
        self._pattern("[0-9]")

    @tatsumasu()
    def _OCT_DIGIT_(self):  # noqa
        self._pattern("[0-7]")

    @tatsumasu()
    def _HEX_DIGIT_(self):  # noqa
        self._pattern("[0-9a-fA-F]")

    @tatsumasu()
    def _BIN_DIGIT_(self):  # noqa
        self._pattern("[01]")

    @tatsumasu()
    def _POINT_FLOAT_(self):  # noqa
        with self._choice():
            with self._option():
                with self._optional():
                    self._INT_PART_()
                self._FRACTION_()
            with self._option():
                self._INT_PART_()
                self._token(".")
            self._error("no available options")

    @tatsumasu()
    def _EXPONENT_FLOAT_(self):  # noqa
        with self._group():
            with self._choice():
                with self._option():
                    self._INT_PART_()
                with self._option():
                    self._POINT_FLOAT_()
                self._error("no available options")
        self._EXPONENT_()

    @tatsumasu()
    def _INT_PART_(self):  # noqa
        def block0():
            self._DIGIT_()

        self._positive_closure(block0)

    @tatsumasu()
    def _FRACTION_(self):  # noqa
        self._token(".")

        def block0():
            self._DIGIT_()

        self._positive_closure(block0)

    @tatsumasu()
    def _EXPONENT_(self):  # noqa
        self._pattern("[eE][+-]?")

        def block0():
            self._DIGIT_()

        self._positive_closure(block0)

    @tatsumasu()
    def _SHORT_BYTES_(self):  # noqa
        self._token("\\'")

        def block0():
            with self._choice():
                with self._option():
                    self._SHORT_BYTES_CHAR_NO_SINGLE_QUOTE_()
                with self._option():
                    self._BYTES_ESCAPE_SEQ_()
                self._error("no available options")

        self._closure(block0)
        self._pattern("[\\'\"]")

        def block2():
            with self._choice():
                with self._option():
                    self._SHORT_BYTES_CHAR_NO_DOUBLE_QUOTE_()
                with self._option():
                    self._BYTES_ESCAPE_SEQ_()
                self._error("no available options")

        self._closure(block2)
        self._token('"')

    @tatsumasu()
    def _LONG_BYTES_(self):  # noqa
        with self._choice():
            with self._option():
                self._token("\\'\\'\\'")
                with self._optional():
                    self._LONG_BYTES_ITEM_()
                self._token("\\'\\'\\'")
            with self._option():
                self._token('"""')
                with self._optional():
                    self._LONG_BYTES_ITEM_()
                self._token('"""')
            self._error("no available options")

    @tatsumasu()
    def _LONG_BYTES_ITEM_(self):  # noqa
        with self._choice():
            with self._option():
                self._LONG_BYTES_CHAR_()
            with self._option():
                self._BYTES_ESCAPE_SEQ_()
            self._error("no available options")

    @tatsumasu()
    def _SHORT_BYTES_CHAR_NO_SINGLE_QUOTE_(self):  # noqa
        with self._choice():
            with self._option():
                self._pattern("[\\u0000-\\u0009]")
            with self._option():
                self._pattern("[\\u000B-\\u000C]")
            with self._option():
                self._pattern("[\\u000E-\\u0026]")
            with self._option():
                self._pattern("[\\u0028-\\u005B]")
            with self._option():
                self._pattern("[\\u005D-\\u007F]")
            self._error("no available options")

    @tatsumasu()
    def _SHORT_BYTES_CHAR_NO_DOUBLE_QUOTE_(self):  # noqa
        with self._choice():
            with self._option():
                self._pattern("[\\u0000-\\u0009]")
            with self._option():
                self._pattern("[\\u000B-\\u000C]")
            with self._option():
                self._pattern("[\\u000E-\\u0021]")
            with self._option():
                self._pattern("[\\u0023-\\u005B]")
            with self._option():
                self._pattern("[\\u005D-\\u007F]")
            self._error("no available options")

    @tatsumasu()
    def _LONG_BYTES_CHAR_(self):  # noqa
        with self._choice():
            with self._option():
                self._pattern("[\\u0000-\\u005B]")
            with self._option():
                self._pattern("[\\u005D-\\u007F]")
            self._error("no available options")

    @tatsumasu()
    def _BYTES_ESCAPE_SEQ_(self):  # noqa
        self._token("\\\\")
        self._pattern("[\\u0000-\\u007F]")

    @tatsumasu()
    def _SPACES_(self):  # noqa
        self._pattern("[ \\t]+")

    @tatsumasu()
    def _COMMENT_(self):  # noqa
        self._token("#")
        self._pattern("[^\\r\\n\\f]*")

    @tatsumasu()
    def _LINE_JOINING_(self):  # noqa
        self._token("\\\\")
        with self._optional():
            self._SPACES_()
        with self._group():
            with self._optional():
                self._token("\\r")
            self._pattern("[\\n\\r\\f]")

    @tatsumasu()
    def _ID_START_(self):  # noqa
        with self._choice():
            with self._option():
                self._token("_")
            with self._option():
                self._pattern("[A-Z]")
            with self._option():
                self._pattern("[a-z]")
            self._error("no available options")

    @tatsumasu()
    def _ID_CONTINUE_(self):  # noqa
        with self._choice():
            with self._option():
                self._ID_START_()
            with self._option():
                self._pattern("[0-9]")
            self._error("no available options")

    @tatsumasu()
    def _INDENT_(self):  # noqa
        with self._ifnot():
            self._void()

    @tatsumasu()
    def _DEDENT_(self):  # noqa
        with self._ifnot():
            self._void()


class UnknownSemantics(object):
    def start(self, ast):  # noqa
        return ast

    def statements(self, ast):  # noqa
        return ast

    def statement(self, ast):  # noqa
        return ast

    def simple_stmt(self, ast):  # noqa
        return ast

    def small_stmt(self, ast):  # noqa
        return ast

    def compound_stmt(self, ast):  # noqa
        return ast

    def assignment(self, ast):  # noqa
        return ast

    def import_stmt(self, ast):  # noqa
        return ast

    def names(self, ast):  # noqa
        return ast

    def if_stmt(self, ast):  # noqa
        return ast

    def elif_block(self, ast):  # noqa
        return ast

    def else_block(self, ast):  # noqa
        return ast

    def while_stmt(self, ast):  # noqa
        return ast

    def with_stmt(self, ast):  # noqa
        return ast

    def return_stmt(self, ast):  # noqa
        return ast

    def function_def(self, ast):  # noqa
        return ast

    def parameters(self, ast):  # noqa
        return ast

    def kwparams(self, ast):  # noqa
        return ast

    def kwparam(self, ast):  # noqa
        return ast

    def param(self, ast):  # noqa
        return ast

    def decorators(self, ast):  # noqa
        return ast

    def class_def(self, ast):  # noqa
        return ast

    def block(self, ast):  # noqa
        return ast

    def full_expressions(self, ast):  # noqa
        return ast

    def full_expression(self, ast):  # noqa
        return ast

    def disjunction(self, ast):  # noqa
        return ast

    def conjunction(self, ast):  # noqa
        return ast

    def comparison(self, ast):  # noqa
        return ast

    def compare_op(self, ast):  # noqa
        return ast

    def bitwise_or(self, ast):  # noqa
        return ast

    def bitwise_and(self, ast):  # noqa
        return ast

    def expressions(self, ast):  # noqa
        return ast

    def expression(self, ast):  # noqa
        return ast

    def term(self, ast):  # noqa
        return ast

    def factor(self, ast):  # noqa
        return ast

    def primary(self, ast):  # noqa
        return ast

    def list(self, ast):  # noqa
        return ast

    def tuple(self, ast):  # noqa
        return ast

    def group(self, ast):  # noqa
        return ast

    def arguments(self, ast):  # noqa
        return ast

    def kwargs(self, ast):  # noqa
        return ast

    def posarg(self, ast):  # noqa
        return ast

    def kwarg(self, ast):  # noqa
        return ast

    def target(self, ast):  # noqa
        return ast

    def STRING(self, ast):  # noqa
        return ast

    def NUMBER(self, ast):  # noqa
        return ast

    def NEWLINE(self, ast):  # noqa
        return ast

    def str(self, ast):  # noqa
        return ast

    def number(self, ast):  # noqa
        return ast

    def integer(self, ast):  # noqa
        return ast

    def newline(self, ast):  # noqa
        return ast

    def NAME(self, ast):  # noqa
        return ast

    def STRING_LITERAL(self, ast):  # noqa
        return ast

    def BYTES_LITERAL(self, ast):  # noqa
        return ast

    def decimal_integer(self, ast):  # noqa
        return ast

    def OCT_INTEGER(self, ast):  # noqa
        return ast

    def HEX_INTEGER(self, ast):  # noqa
        return ast

    def BIN_INTEGER(self, ast):  # noqa
        return ast

    def float_number(self, ast):  # noqa
        return ast

    def IMAG_NUMBER(self, ast):  # noqa
        return ast

    def skip_(self, ast):  # noqa
        return ast

    def unknown_char(self, ast):  # noqa
        return ast

    def SHORT_STRING(self, ast):  # noqa
        return ast

    def LONG_STRING(self, ast):  # noqa
        return ast

    def LONG_STRING_ITEM(self, ast):  # noqa
        return ast

    def LONG_STRING_CHAR(self, ast):  # noqa
        return ast

    def STRING_ESCAPE_SEQ(self, ast):  # noqa
        return ast

    def NON_ZERO_DIGIT(self, ast):  # noqa
        return ast

    def DIGIT(self, ast):  # noqa
        return ast

    def OCT_DIGIT(self, ast):  # noqa
        return ast

    def HEX_DIGIT(self, ast):  # noqa
        return ast

    def BIN_DIGIT(self, ast):  # noqa
        return ast

    def POINT_FLOAT(self, ast):  # noqa
        return ast

    def EXPONENT_FLOAT(self, ast):  # noqa
        return ast

    def INT_PART(self, ast):  # noqa
        return ast

    def FRACTION(self, ast):  # noqa
        return ast

    def EXPONENT(self, ast):  # noqa
        return ast

    def SHORT_BYTES(self, ast):  # noqa
        return ast

    def LONG_BYTES(self, ast):  # noqa
        return ast

    def LONG_BYTES_ITEM(self, ast):  # noqa
        return ast

    def SHORT_BYTES_CHAR_NO_SINGLE_QUOTE(self, ast):  # noqa
        return ast

    def SHORT_BYTES_CHAR_NO_DOUBLE_QUOTE(self, ast):  # noqa
        return ast

    def LONG_BYTES_CHAR(self, ast):  # noqa
        return ast

    def BYTES_ESCAPE_SEQ(self, ast):  # noqa
        return ast

    def SPACES(self, ast):  # noqa
        return ast

    def COMMENT(self, ast):  # noqa
        return ast

    def LINE_JOINING(self, ast):  # noqa
        return ast

    def ID_START(self, ast):  # noqa
        return ast

    def ID_CONTINUE(self, ast):  # noqa
        return ast

    def INDENT(self, ast):  # noqa
        return ast

    def DEDENT(self, ast):  # noqa
        return ast


def main(filename, start=None, **kwargs):
    if start is None:
        start = "start"
    if not filename or filename == "-":
        text = sys.stdin.read()
    else:
        with open(filename) as f:
            text = f.read()
    parser = UnknownParser()
    return parser.parse(text, rule_name=start, filename=filename, **kwargs)


if __name__ == "__main__":
    import json
    from tatsu.util import asjson

    ast = generic_main(main, UnknownParser, name="Unknown")
    print("AST:")
    print(ast)
    print()
    print("JSON:")
    print(json.dumps(asjson(ast), indent=2))
    print()
