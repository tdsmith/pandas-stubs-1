from typing import (
    Any,
    Hashable,
)

import numpy as np
from pandas.core.computation.pytables import PyTablesExpr
from pandas.core.frame import DataFrame
from pandas.core.generic import NDFrame
from pandas.core.indexes.base import Index
from pandas.core.indexes.multi import MultiIndex
from pandas.core.series import Series

from pandas._typing import (
    ArrayLike,
    FilePathOrBuffer,
)

from pandas.core.dtypes.generic import ABCExtensionArray

# pytables may not be installed so create them as dummy classes
class Col: ...
class Node: ...

Term = PyTablesExpr

class PossibleDataLossError(Exception): ...
class ClosedFileError(Exception): ...
class IncompatibilityWarning(Warning): ...

incompatibility_doc: str

class AttributeConflictWarning(Warning): ...

attribute_conflict_doc: str

class DuplicateWarning(Warning): ...

duplicate_doc: str
performance_doc: str
dropna_doc: str
format_doc: str

def to_hdf(
    path_or_buf: FilePathOrBuffer,
    key: str,
    value: NDFrame,
    mode: str = ...,
    complevel: int | None = ...,
    complib: str | None = ...,
    append: bool = ...,
    format: str | None = ...,
    index: bool = ...,
    min_itemsize: int | dict[str, int] | None = ...,
    nan_rep=...,
    dropna: bool | None = ...,
    data_columns: list[str] | None = ...,
    errors: str = ...,
    encoding: str = ...,
): ...
def read_hdf(
    path_or_buf: FilePathOrBuffer,
    key=...,
    mode: str = ...,
    errors: str = ...,
    where: list[Any] | None = ...,
    start: int | None = ...,
    stop: int | None = ...,
    columns: list[str] | None = ...,
    iterator: bool = ...,
    chunksize: int | None = ...,
    **kwargs,
): ...

class HDFStore:
    def __init__(
        self,
        path,
        mode: str = ...,
        complevel: int | None = ...,
        complib=...,
        fletcher32: bool = ...,
        **kwargs,
    ) -> None: ...
    def __fspath__(self): ...
    @property
    def root(self): ...
    @property
    def filename(self): ...
    def __getitem__(self, key: str): ...
    def __setitem__(self, key: str, value): ...
    def __delitem__(self, key: str): ...
    def __getattr__(self, name: str): ...
    def __contains__(self, key: str) -> bool: ...
    def __len__(self) -> int: ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, traceback) -> None: ...
    def keys(self) -> list[str]: ...
    def __iter__(self): ...
    def items(self) -> None: ...
    iteritems = ...
    def open(self, mode: str = ..., **kwargs): ...
    def close(self) -> None: ...
    @property
    def is_open(self) -> bool: ...
    def flush(self, fsync: bool = ...): ...
    def get(self, key: str): ...
    def select(
        self,
        key: str,
        where=...,
        start=...,
        stop=...,
        columns=...,
        iterator=...,
        chunksize=...,
        auto_close: bool = ...,
    ): ...
    def select_as_coordinates(
        self, key: str, where=..., start: int | None = ..., stop: int | None = ...
    ): ...
    def select_column(
        self,
        key: str,
        column: str,
        start: int | None = ...,
        stop: int | None = ...,
    ): ...
    def select_as_multiple(
        self,
        keys,
        where=...,
        selector=...,
        columns=...,
        start=...,
        stop=...,
        iterator=...,
        chunksize=...,
        auto_close: bool = ...,
    ): ...
    def put(
        self,
        key: str,
        value: NDFrame,
        format=...,
        index=...,
        append=...,
        complib=...,
        complevel: int | None = ...,
        min_itemsize: int | dict[str, int] | None = ...,
        nan_rep=...,
        data_columns: list[str] | None = ...,
        encoding=...,
        errors: str = ...,
    ): ...
    def remove(self, key: str, where=..., start=..., stop=...): ...
    def append(
        self,
        key: str,
        value: NDFrame,
        format=...,
        axes=...,
        index=...,
        append=...,
        complib=...,
        complevel: int | None = ...,
        columns=...,
        min_itemsize: int | dict[str, int] | None = ...,
        nan_rep=...,
        chunksize=...,
        expectedrows=...,
        dropna: bool | None = ...,
        data_columns: list[str] | None = ...,
        encoding=...,
        errors: str = ...,
    ): ...
    def append_to_multiple(
        self, d: dict, value, selector, data_columns=..., axes=..., dropna=..., **kwargs
    ): ...
    def create_table_index(
        self,
        key: str,
        columns=...,
        optlevel: int | None = ...,
        kind: str | None = ...,
    ): ...
    def groups(self): ...
    def walk(self, where: str = ...) -> None: ...
    def get_node(self, key: str) -> Node | None: ...
    def get_storer(self, key: str) -> GenericFixed | Table: ...
    def copy(
        self,
        file,
        mode=...,
        propindexes: bool = ...,
        keys=...,
        complib=...,
        complevel: int | None = ...,
        fletcher32: bool = ...,
        overwrite=...,
    ): ...
    def info(self) -> str: ...

class TableIterator:
    chunksize: int | None
    store: HDFStore
    s: GenericFixed | Table
    func = ...
    where = ...
    nrows = ...
    start = ...
    stop = ...
    coordinates = ...
    auto_close = ...
    def __init__(
        self,
        store: HDFStore,
        s: GenericFixed | Table,
        func,
        where,
        nrows,
        start=...,
        stop=...,
        iterator: bool = ...,
        chunksize: int | None = ...,
        auto_close: bool = ...,
    ) -> None: ...
    def __iter__(self): ...
    def close(self) -> None: ...
    def get_result(self, coordinates: bool = ...): ...

class IndexCol:
    is_an_indexable: bool = ...
    is_data_indexable: bool = ...
    name: str
    cname: str
    values = ...
    kind = ...
    typ = ...
    axis = ...
    pos = ...
    freq = ...
    tz = ...
    index_name = ...
    ordered = ...
    table = ...
    meta = ...
    metadata = ...
    def __init__(
        self,
        name: str,
        values=...,
        kind=...,
        typ=...,
        cname: str | None = ...,
        axis=...,
        pos=...,
        freq=...,
        tz=...,
        index_name=...,
        ordered=...,
        table=...,
        meta=...,
        metadata=...,
    ) -> None: ...
    @property
    def itemsize(self) -> int: ...
    @property
    def kind_attr(self) -> str: ...
    def set_pos(self, pos: int): ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    @property
    def is_indexed(self) -> bool: ...
    def convert(self, values: np.ndarray, nan_rep, encoding: str, errors: str): ...
    def take_data(self): ...
    @property
    def attrs(self): ...
    @property
    def description(self): ...
    @property
    def col(self): ...
    @property
    def cvalues(self): ...
    def __iter__(self): ...
    def maybe_set_size(self, min_itemsize=...) -> None: ...
    def validate_names(self) -> None: ...
    def validate_and_set(self, handler: AppendableTable, append: bool): ...
    def validate_col(self, itemsize=...): ...
    def validate_attr(self, append: bool): ...
    def update_info(self, info) -> None: ...
    def set_info(self, info) -> None: ...
    def set_attr(self) -> None: ...
    def validate_metadata(self, handler: AppendableTable): ...
    def write_metadata(self, handler: AppendableTable): ...

class GenericIndexCol(IndexCol):
    @property
    def is_indexed(self) -> bool: ...
    def convert(self, values: np.ndarray, nan_rep, encoding: str, errors: str): ...
    def set_attr(self) -> None: ...

class DataCol(IndexCol):
    is_an_indexable: bool = ...
    is_data_indexable: bool = ...
    dtype = ...
    data = ...
    def __init__(
        self,
        name: str,
        values=...,
        kind=...,
        typ=...,
        cname=...,
        pos=...,
        tz=...,
        ordered=...,
        table=...,
        meta=...,
        metadata=...,
        dtype=...,
        data=...,
    ) -> None: ...
    @property
    def dtype_attr(self) -> str: ...
    @property
    def meta_attr(self) -> str: ...
    def __eq__(self, other) -> bool: ...
    kind = ...
    def set_data(self, data: np.ndarray | ABCExtensionArray): ...
    def take_data(self): ...
    @classmethod
    def get_atom_string(cls, shape, itemsize): ...
    @classmethod
    def get_atom_coltype(cls, kind: str) -> type[Col]: ...
    @classmethod
    def get_atom_data(cls, shape, kind: str) -> Col: ...
    @classmethod
    def get_atom_datetime64(cls, shape): ...
    @classmethod
    def get_atom_timedelta64(cls, shape): ...
    @property
    def shape(self): ...
    @property
    def cvalues(self): ...
    def validate_attr(self, append) -> None: ...
    def convert(self, values: np.ndarray, nan_rep, encoding: str, errors: str): ...
    def set_attr(self) -> None: ...

class DataIndexableCol(DataCol):
    is_data_indexable: bool = ...
    def validate_names(self) -> None: ...
    @classmethod
    def get_atom_string(cls, shape, itemsize): ...
    @classmethod
    def get_atom_data(cls, shape, kind: str) -> Col: ...
    @classmethod
    def get_atom_datetime64(cls, shape): ...
    @classmethod
    def get_atom_timedelta64(cls, shape): ...

class GenericDataIndexableCol(DataIndexableCol): ...

class Fixed:
    pandas_kind: str
    format_type: str = ...
    obj_type: type[DataFrame | Series]
    ndim: int
    encoding: str
    parent: HDFStore
    group: Node
    errors: str
    is_table: bool = ...
    def __init__(
        self, parent: HDFStore, group: Node, encoding: str = ..., errors: str = ...
    ) -> None: ...
    @property
    def is_old_version(self) -> bool: ...
    @property
    def version(self) -> tuple[int, int, int]: ...
    @property
    def pandas_type(self): ...
    def set_object_info(self) -> None: ...
    def copy(self): ...
    @property
    def shape(self): ...
    @property
    def pathname(self): ...
    @property
    def attrs(self): ...
    def set_attrs(self) -> None: ...
    def get_attrs(self) -> None: ...
    @property
    def storable(self): ...
    @property
    def is_exists(self) -> bool: ...
    @property
    def nrows(self): ...
    def validate(self, other): ...
    def validate_version(self, where=...): ...
    def infer_axes(self): ...
    def read(
        self,
        where=...,
        columns=...,
        start: int | None = ...,
        stop: int | None = ...,
    ): ...
    def delete(self, where=..., start: int | None = ..., stop: int | None = ...): ...

class GenericFixed(Fixed):
    attributes: list[str] = ...
    def validate_read(self, columns, where) -> None: ...
    @property
    def is_exists(self) -> bool: ...
    def set_attrs(self) -> None: ...
    def get_attrs(self) -> None: ...
    def write(self, obj, **kwargs) -> None: ...
    def read_array(self, key: str, start: int | None = ..., stop: int | None = ...): ...
    def read_index(
        self, key: str, start: int | None = ..., stop: int | None = ...
    ) -> Index: ...
    def write_index(self, key: str, index: Index): ...
    def write_multi_index(self, key: str, index: MultiIndex): ...
    def read_multi_index(
        self, key: str, start: int | None = ..., stop: int | None = ...
    ) -> MultiIndex: ...
    def read_index_node(
        self, node: Node, start: int | None = ..., stop: int | None = ...
    ) -> Index: ...
    def write_array_empty(self, key: str, value: ArrayLike): ...
    def write_array(self, key: str, value: ArrayLike, items: Index | None = ...): ...

class SeriesFixed(GenericFixed):
    pandas_kind: str = ...
    name: Hashable | None
    @property
    def shape(self): ...
    def read(
        self,
        where=...,
        columns=...,
        start: int | None = ...,
        stop: int | None = ...,
    ): ...
    def write(self, obj, **kwargs) -> None: ...

class BlockManagerFixed(GenericFixed):
    nblocks: int
    @property
    def shape(self): ...
    def read(
        self,
        where=...,
        columns=...,
        start: int | None = ...,
        stop: int | None = ...,
    ): ...
    def write(self, obj, **kwargs) -> None: ...

class FrameFixed(BlockManagerFixed):
    pandas_kind: str = ...

class Table(Fixed):
    pandas_kind: str = ...
    format_type: str = ...
    table_type: str
    levels: int = ...
    is_table: bool = ...
    index_axes: list[IndexCol]
    non_index_axes: list[tuple[int, Any]]
    values_axes: list[DataCol]
    data_columns: list
    metadata: list
    info: dict
    nan_rep = ...
    def __init__(
        self,
        parent: HDFStore,
        group: Node,
        encoding=...,
        errors: str = ...,
        index_axes=...,
        non_index_axes=...,
        values_axes=...,
        data_columns=...,
        info=...,
        nan_rep=...,
    ) -> None: ...
    @property
    def table_type_short(self) -> str: ...
    def __getitem__(self, c: str): ...
    def validate(self, other) -> None: ...
    @property
    def is_multi_index(self) -> bool: ...
    def validate_multiindex(self, obj): ...
    @property
    def nrows_expected(self) -> int: ...
    @property
    def is_exists(self) -> bool: ...
    @property
    def storable(self): ...
    @property
    def table(self): ...
    @property
    def dtype(self): ...
    @property
    def description(self): ...
    @property
    def axes(self): ...
    @property
    def ncols(self) -> int: ...
    @property
    def is_transposed(self) -> bool: ...
    @property
    def data_orientation(self): ...
    def queryables(self) -> dict[str, Any]: ...
    def index_cols(self): ...
    def values_cols(self) -> list[str]: ...
    def write_metadata(self, key: str, values: np.ndarray): ...
    def read_metadata(self, key: str): ...
    def set_attrs(self) -> None: ...
    def get_attrs(self) -> None: ...
    def validate_version(self, where=...) -> None: ...
    def validate_min_itemsize(self, min_itemsize) -> None: ...
    def indexables(self): ...
    def create_index(self, columns=..., optlevel=..., kind: str | None = ...): ...
    @classmethod
    def get_object(cls, obj, transposed: bool): ...
    def validate_data_columns(self, data_columns, min_itemsize, non_index_axes): ...
    def process_axes(self, obj, selection: Selection, columns=...): ...
    def create_description(
        self,
        complib,
        complevel: int | None,
        fletcher32: bool,
        expectedrows: int | None,
    ) -> dict[str, Any]: ...
    def read_coordinates(
        self, where=..., start: int | None = ..., stop: int | None = ...
    ): ...
    def read_column(
        self,
        column: str,
        where=...,
        start: int | None = ...,
        stop: int | None = ...,
    ): ...

class WORMTable(Table):
    table_type: str = ...
    def read(
        self,
        where=...,
        columns=...,
        start: int | None = ...,
        stop: int | None = ...,
    ): ...
    def write(self, **kwargs) -> None: ...

class AppendableTable(Table):
    table_type: str = ...
    def write(
        self,
        obj,
        axes=...,
        append: bool = ...,
        complib=...,
        complevel=...,
        fletcher32=...,
        min_itemsize=...,
        chunksize=...,
        expectedrows=...,
        dropna: bool = ...,
        nan_rep=...,
        data_columns=...,
    ) -> None: ...
    def write_data(self, chunksize: int | None, dropna: bool = ...): ...
    def write_data_chunk(
        self,
        rows: np.ndarray,
        indexes: list[np.ndarray],
        mask: np.ndarray | None,
        values: list[np.ndarray],
    ): ...
    def delete(self, where=..., start: int | None = ..., stop: int | None = ...): ...

class AppendableFrameTable(AppendableTable):
    pandas_kind: str = ...
    table_type: str = ...
    ndim: int = ...
    obj_type: type[DataFrame | Series] = ...
    @property
    def is_transposed(self) -> bool: ...
    @classmethod
    def get_object(cls, obj, transposed: bool): ...
    def read(
        self,
        where=...,
        columns=...,
        start: int | None = ...,
        stop: int | None = ...,
    ): ...

class AppendableSeriesTable(AppendableFrameTable):
    pandas_kind: str = ...
    table_type: str = ...
    ndim: int = ...
    @property
    def is_transposed(self) -> bool: ...
    @classmethod
    def get_object(cls, obj, transposed: bool): ...
    def write(self, obj, data_columns=..., **kwargs): ...
    def read(
        self,
        where=...,
        columns=...,
        start: int | None = ...,
        stop: int | None = ...,
    ) -> Series: ...

class AppendableMultiSeriesTable(AppendableSeriesTable):
    pandas_kind: str = ...
    table_type: str = ...
    def write(self, obj, **kwargs): ...

class GenericTable(AppendableFrameTable):
    pandas_kind: str = ...
    table_type: str = ...
    ndim: int = ...
    @property
    def pandas_type(self) -> str: ...
    @property
    def storable(self): ...
    nan_rep = ...
    def get_attrs(self) -> None: ...
    def indexables(self): ...

class AppendableMultiFrameTable(AppendableFrameTable):
    table_type: str = ...
    ndim: int = ...
    @property
    def table_type_short(self) -> str: ...
    def write(self, obj, data_columns=..., **kwargs): ...
    def read(
        self,
        where=...,
        columns=...,
        start: int | None = ...,
        stop: int | None = ...,
    ): ...

class Selection:
    table = ...
    where = ...
    start = ...
    stop = ...
    condition = ...
    filter = ...
    terms = ...
    coordinates = ...
    def __init__(
        self,
        table: Table,
        where=...,
        start: int | None = ...,
        stop: int | None = ...,
    ) -> None: ...
    def generate(self, where): ...
    def select(self): ...
    def select_coords(self): ...
