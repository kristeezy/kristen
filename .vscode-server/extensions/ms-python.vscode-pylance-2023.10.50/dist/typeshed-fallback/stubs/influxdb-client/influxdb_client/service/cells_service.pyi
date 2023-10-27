from _typeshed import Incomplete

from influxdb_client.service._base_service import _BaseService

class CellsService(_BaseService):
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    def delete_dashboards_id_cells_id(self, dashboard_id, cell_id, **kwargs): ...
    def delete_dashboards_id_cells_id_with_http_info(self, dashboard_id, cell_id, **kwargs): ...
    async def delete_dashboards_id_cells_id_async(self, dashboard_id, cell_id, **kwargs): ...
    def get_dashboards_id_cells_id_view(self, dashboard_id, cell_id, **kwargs): ...
    def get_dashboards_id_cells_id_view_with_http_info(self, dashboard_id, cell_id, **kwargs): ...
    async def get_dashboards_id_cells_id_view_async(self, dashboard_id, cell_id, **kwargs): ...
    def patch_dashboards_id_cells_id(self, dashboard_id, cell_id, cell_update, **kwargs): ...
    def patch_dashboards_id_cells_id_with_http_info(self, dashboard_id, cell_id, cell_update, **kwargs): ...
    async def patch_dashboards_id_cells_id_async(self, dashboard_id, cell_id, cell_update, **kwargs): ...
    def patch_dashboards_id_cells_id_view(self, dashboard_id, cell_id, view, **kwargs): ...
    def patch_dashboards_id_cells_id_view_with_http_info(self, dashboard_id, cell_id, view, **kwargs): ...
    async def patch_dashboards_id_cells_id_view_async(self, dashboard_id, cell_id, view, **kwargs): ...
    def post_dashboards_id_cells(self, dashboard_id, create_cell, **kwargs): ...
    def post_dashboards_id_cells_with_http_info(self, dashboard_id, create_cell, **kwargs): ...
    async def post_dashboards_id_cells_async(self, dashboard_id, create_cell, **kwargs): ...
    def put_dashboards_id_cells(self, dashboard_id, cell, **kwargs): ...
    def put_dashboards_id_cells_with_http_info(self, dashboard_id, cell, **kwargs): ...
    async def put_dashboards_id_cells_async(self, dashboard_id, cell, **kwargs): ...
