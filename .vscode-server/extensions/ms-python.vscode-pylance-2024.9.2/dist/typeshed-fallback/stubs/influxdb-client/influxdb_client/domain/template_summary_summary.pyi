from _typeshed import Incomplete

class TemplateSummarySummary:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        buckets: Incomplete | None = None,
        checks: Incomplete | None = None,
        dashboards: Incomplete | None = None,
        labels: Incomplete | None = None,
        label_mappings: Incomplete | None = None,
        missing_env_refs: Incomplete | None = None,
        missing_secrets: Incomplete | None = None,
        notification_endpoints: Incomplete | None = None,
        notification_rules: Incomplete | None = None,
        tasks: Incomplete | None = None,
        telegraf_configs: Incomplete | None = None,
        variables: Incomplete | None = None,
    ) -> None: ...
    @property
    def buckets(self): ...
    @buckets.setter
    def buckets(self, buckets) -> None: ...
    @property
    def checks(self): ...
    @checks.setter
    def checks(self, checks) -> None: ...
    @property
    def dashboards(self): ...
    @dashboards.setter
    def dashboards(self, dashboards) -> None: ...
    @property
    def labels(self): ...
    @labels.setter
    def labels(self, labels) -> None: ...
    @property
    def label_mappings(self): ...
    @label_mappings.setter
    def label_mappings(self, label_mappings) -> None: ...
    @property
    def missing_env_refs(self): ...
    @missing_env_refs.setter
    def missing_env_refs(self, missing_env_refs) -> None: ...
    @property
    def missing_secrets(self): ...
    @missing_secrets.setter
    def missing_secrets(self, missing_secrets) -> None: ...
    @property
    def notification_endpoints(self): ...
    @notification_endpoints.setter
    def notification_endpoints(self, notification_endpoints) -> None: ...
    @property
    def notification_rules(self): ...
    @notification_rules.setter
    def notification_rules(self, notification_rules) -> None: ...
    @property
    def tasks(self): ...
    @tasks.setter
    def tasks(self, tasks) -> None: ...
    @property
    def telegraf_configs(self): ...
    @telegraf_configs.setter
    def telegraf_configs(self, telegraf_configs) -> None: ...
    @property
    def variables(self): ...
    @variables.setter
    def variables(self, variables) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
