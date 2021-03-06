from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from meiduo_admin.views import users, statistical, channels, skus, spus, orders, permissions

urlpatterns = [
    url(r'^authorizations/$', users.AdminAuthorizeView.as_view()),
    url(r'^statistical/total_count/$', statistical.UserTotalCountView.as_view()),
    url(r'^statistical/day_increment/$', statistical.UserDayIncrementView.as_view()),
    url(r'^statistical/day_active/$', statistical.UserDayActiveView.as_view()),
    url(r'^statistical/day_orders/$', statistical.UserDayOrdersView.as_view()),
    url(r'^statistical/month_increment/$', statistical.UserMonthCountView.as_view()),
    url(r'^statistical/goods_day_views/$', statistical.GoodsDayView.as_view()),
    url(r'^users/$', users.UserInfoView.as_view()),
    # 频道管理
    url(r'^goods/channel_types/$', channels.ChannelTypesView.as_view()),
    # 频道管理
    url(r'^goods/categories/$', channels.ChannelCategoriesView.as_view()),
    # 图片管理
    url(r'^skus/simple/$', skus.SKUSimpleView.as_view()),
    url(r'^goods/simple/$', spus.SPUSimpleView.as_view()),
    url(r'^goods/(?P<pk>\d+)/specs/$', spus.SPUSpecView.as_view()),
    # 权限管理
    url(r'^permission/content_types/$', permissions.PermissionViewSet.as_view({
        'get': 'content_types'
    })),
    # 用户组管理
    url(r'^permission/simple/$', permissions.GroupViewSet.as_view({
        'get': 'simple'
    })),
    # 管理员管理
    url(r'^permission/groups/simple/$', permissions.AdminViewSet.as_view({
        'get': 'simple'
    })),
    url(r'^goods/brands/simple/$',spus.SPUBrandsSimple.as_view()),
    url(r'^goods/channel/categories/$',spus.SPUCategoriesSimple.as_view()),
    url(r'^goods/channel/categories/(?P<pk>\d+)/$',spus.SPUSubCategoriesSimple.as_view()),
    url(r'^goods/specs/simple/$', spus.SpecsSimple.as_view()),
]


router = DefaultRouter()
router.register('goods/channels',channels.ChannelViewSet,base_name='channels')
urlpatterns += router.urls

# 图片管理
router = DefaultRouter()
router.register(r'skus/images', skus.SKUImageViewSet, base_name='images')
urlpatterns += router.urls

router = DefaultRouter()
router.register('skus', skus.SKUViewSet, base_name='skus')
urlpatterns += router.urls


# 订单管理
router = DefaultRouter()
router.register('orders', orders.OrdersViewSet, base_name='orders')
urlpatterns += router.urls


# 权限管理
router = DefaultRouter()
router.register('permission/perms', permissions.PermissionViewSet, base_name='perms')
urlpatterns += router.urls


# 用户组管理
router = DefaultRouter()
router.register('permission/groups', permissions.GroupViewSet, base_name='groups')
urlpatterns += router.urls


# 管理员管理
router = DefaultRouter()
router.register('permission/admins', permissions.AdminViewSet, base_name='admins')
urlpatterns += router.urls

# SPU商品规格管理
router = DefaultRouter()
router.register('goods/specs', spus.GoodsSpecsViewSet, base_name='specs')
urlpatterns += router.urls

# 品牌管理
router = DefaultRouter()
router.register('goods/brands', spus.GoodsBrandViewSet, base_name='brands')
urlpatterns += router.urls

# SPU管理
router = DefaultRouter()
router.register('goods', spus.SPUViewSet, base_name='goods')
urlpatterns += router.urls


# SPU管理
router = DefaultRouter()
router.register('specs/options', spus.SpecsOptionsViewSet, base_name='options')
urlpatterns += router.urls
