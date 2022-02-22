"""ViewBuilder."""
from typing import Dict

from hive_metastore_client.builders.abstract_builder import AbstractBuilder
from thrift_files.libraries.thrift_hive_metastore_client.ttypes import (  # type: ignore # noqa: E501
    Table,
    PrincipalPrivilegeSet,
    CreationMetadata,
    PrincipalType,
    StorageDescriptor,
)


class ViewBuilder(AbstractBuilder):
    """Builds thrift Table object configured as a Virtual View."""

    def __init__(
        self,
        view_name: str,
        db_name: str,
        storage_descriptor: StorageDescriptor,
        owner: str = None,
        create_time: int = None,
        last_access_time: int = None,
        retention: int = None,
        parameters: Dict[str, str] = None,
        view_original_text: str = None,
        view_expanded_text: str = None,
        privileges: PrincipalPrivilegeSet = None,
        temporary: bool = False,
        rewrite_enabled: bool = None,
        creation_metadata: CreationMetadata = None,
        cat_name: str = None,
        owner_type: PrincipalType = PrincipalType.USER,
    ) -> None:
        """
        Constructor.

        :param view_name: the table name
        :param db_name: the database name
        :param storage_descriptor: StorageDescriptor object
        :param owner: owner of this table
        :param create_time: creation timestamp of the table
        :param last_access_time: last access timestamp (usually this will be filled
        from HDFS and shouldn't be relied on)
        :param retention: retention timestamp
        :param parameters: to store comments or any other user level parameters
        :param view_original_text: original view text, null for non-view
        :param view_expanded_text: expanded view text, null for non-view
        :param privileges:  privilege grant info (PrincipalPrivilegeSet object)
        :param temporary: whether it is temporary or not
        :param rewrite_enabled: rewrite enabled or not
        :param creation_metadata: only for MVs, it stores table names used and
        txn list at MV creation
        :param cat_name: name of the catalog the table is in
        :param owner_type: owner type of this table (default to USER for
        backward compatibility)
        """
        self.view_name = view_name
        self.db_name = db_name
        self.owner = owner
        self.create_time = create_time
        self.last_access_time = last_access_time
        self.retention = retention
        self.storage_descriptor = storage_descriptor
        self.parameters = {} if parameters is None else parameters
        self.view_original_text = view_original_text
        self.view_expanded_text = view_expanded_text
        self.privileges = privileges
        self.temporary = temporary
        self.rewrite_enabled = rewrite_enabled
        self.creation_metadata = creation_metadata
        self.cat_name = cat_name
        self.owner_type = owner_type
        self.table_type = "VIRTUAL_VIEW"

    def build(self) -> Table:
        """Returns the thrift Table object."""
        return Table(
            tableName=self.view_name,
            dbName=self.db_name,
            owner=self.owner,
            createTime=self.create_time,
            lastAccessTime=self.last_access_time,
            retention=self.retention,
            sd=self.storage_descriptor,
            parameters=self.parameters,
            viewOriginalText=self.view_original_text,
            viewExpandedText=self.view_expanded_text,
            tableType=self.table_type,
            privileges=self.privileges,
            temporary=self.temporary,
            rewriteEnabled=self.rewrite_enabled,
            creationMetadata=self.creation_metadata,
            catName=self.cat_name,
            ownerType=self.owner_type,
        )
