from _typeshed import Incomplete

from hvac.api.vault_api_base import VaultApiBase

logger: Incomplete

class Aws(VaultApiBase):
    def configure(
        self,
        max_retries: Incomplete | None = None,
        access_key: Incomplete | None = None,
        secret_key: Incomplete | None = None,
        endpoint: Incomplete | None = None,
        iam_endpoint: Incomplete | None = None,
        sts_endpoint: Incomplete | None = None,
        iam_server_id_header_value: Incomplete | None = None,
        mount_point: str = "aws",
        sts_region: str | None = None,
    ): ...
    def read_config(self, mount_point: str = "aws"): ...
    def delete_config(self, mount_point: str = "aws"): ...
    def configure_identity_integration(
        self,
        iam_alias: Incomplete | None = None,
        ec2_alias: Incomplete | None = None,
        mount_point: str = "aws",
        iam_metadata: str | list[str] | None = None,
        ec2_metadata: str | list[str] | None = None,
    ): ...
    def read_identity_integration(self, mount_point: str = "aws"): ...
    def create_certificate_configuration(
        self, cert_name, aws_public_cert, document_type: Incomplete | None = None, mount_point: str = "aws"
    ): ...
    def read_certificate_configuration(self, cert_name, mount_point: str = "aws"): ...
    def delete_certificate_configuration(self, cert_name, mount_point: str = "aws"): ...
    def list_certificate_configurations(self, mount_point: str = "aws"): ...
    def create_sts_role(self, account_id, sts_role, mount_point: str = "aws"): ...
    def read_sts_role(self, account_id, mount_point: str = "aws"): ...
    def list_sts_roles(self, mount_point: str = "aws"): ...
    def delete_sts_role(self, account_id, mount_point: str = "aws"): ...
    def configure_identity_whitelist_tidy(
        self, safety_buffer: Incomplete | None = None, disable_periodic_tidy: Incomplete | None = None, mount_point: str = "aws"
    ): ...
    def read_identity_whitelist_tidy(self, mount_point: str = "aws"): ...
    def delete_identity_whitelist_tidy(self, mount_point: str = "aws"): ...
    def configure_role_tag_blacklist_tidy(
        self, safety_buffer: Incomplete | None = None, disable_periodic_tidy: Incomplete | None = None, mount_point: str = "aws"
    ): ...
    def read_role_tag_blacklist_tidy(self, mount_point: str = "aws"): ...
    def delete_role_tag_blacklist_tidy(self, mount_point: str = "aws"): ...
    def create_role(
        self,
        role,
        auth_type: Incomplete | None = None,
        bound_ami_id: Incomplete | None = None,
        bound_account_id: Incomplete | None = None,
        bound_region: Incomplete | None = None,
        bound_vpc_id: Incomplete | None = None,
        bound_subnet_id: Incomplete | None = None,
        bound_iam_role_arn: Incomplete | None = None,
        bound_iam_instance_profile_arn: Incomplete | None = None,
        bound_ec2_instance_id: Incomplete | None = None,
        role_tag: Incomplete | None = None,
        bound_iam_principal_arn: Incomplete | None = None,
        inferred_entity_type: Incomplete | None = None,
        inferred_aws_region: Incomplete | None = None,
        resolve_aws_unique_ids: Incomplete | None = None,
        ttl: Incomplete | None = None,
        max_ttl: Incomplete | None = None,
        period: Incomplete | None = None,
        policies: Incomplete | None = None,
        allow_instance_migration: Incomplete | None = None,
        disallow_reauthentication: Incomplete | None = None,
        mount_point: str = "aws",
    ): ...
    def read_role(self, role, mount_point: str = "aws"): ...
    def list_roles(self, mount_point: str = "aws"): ...
    def delete_role(self, role, mount_point: str = "aws"): ...
    def create_role_tags(
        self,
        role,
        policies: Incomplete | None = None,
        max_ttl: Incomplete | None = None,
        instance_id: Incomplete | None = None,
        allow_instance_migration: Incomplete | None = None,
        disallow_reauthentication: Incomplete | None = None,
        mount_point: str = "aws",
    ): ...
    def iam_login(
        self,
        access_key,
        secret_key,
        session_token: Incomplete | None = None,
        header_value: Incomplete | None = None,
        role: Incomplete | None = None,
        use_token: bool = True,
        region: str = "us-east-1",
        mount_point: str = "aws",
    ): ...
    def ec2_login(
        self,
        pkcs7,
        nonce: Incomplete | None = None,
        role: Incomplete | None = None,
        use_token: bool = True,
        mount_point: str = "aws",
    ): ...
    def place_role_tags_in_blacklist(self, role_tag, mount_point: str = "aws"): ...
    def read_role_tag_blacklist(self, role_tag, mount_point: str = "aws"): ...
    def list_blacklist_tags(self, mount_point: str = "aws"): ...
    def delete_blacklist_tags(self, role_tag, mount_point: str = "aws"): ...
    def tidy_blacklist_tags(self, safety_buffer: str = "72h", mount_point: str = "aws"): ...
    def read_identity_whitelist(self, instance_id, mount_point: str = "aws"): ...
    def list_identity_whitelist(self, mount_point: str = "aws"): ...
    def delete_identity_whitelist_entries(self, instance_id, mount_point: str = "aws"): ...
    def tidy_identity_whitelist_entries(self, safety_buffer: str = "72h", mount_point: str = "aws"): ...
