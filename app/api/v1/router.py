from fastapi import APIRouter

from app.api.v1.endpoints.activity import activity,insights,metrics,users
router=APIRouter

router.include_router(activity.router,prefix='/activity',tags=['Activity'])
router.include_router(insights.router,prefix='/insights',tags=['Insights'])
router.include_router(metrics.router,prefix='/metrics',tags=['Metrics'])
router.include_router(users.router,prefix='/users',tags=['Users'])