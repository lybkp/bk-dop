# -*- coding: utf-8 -*-
from django.conf import settings

BK_PAAS_HOST = settings.BK_PAAS_INNER_HOST or settings.BK_PAAS_HOST or ""
ESB_PREFIX = "/api/c/compapi/"
ESB_PREFIX_V2 = "/api/c/compapi/v2/"
SELF_API_PREFIX = "/api/c/self-service-api/"

# 蓝鲸平台模块域名
JOB_APIGATEWAY_ROOT = BK_PAAS_HOST + ESB_PREFIX + "job/"
BK_LOGIN_APIGATEWAY_ROOT = BK_PAAS_HOST + ESB_PREFIX + "bk_login/"
BK_PAAS_APIGATEWAY_ROOT = BK_PAAS_HOST + ESB_PREFIX + "bk_paas/"
CC_APIGATEWAY_ROOT = BK_PAAS_HOST + ESB_PREFIX + "cc/"

CC_APIGATEWAY_ROOT_V2 = BK_PAAS_HOST + ESB_PREFIX_V2 + "cc/"
GSE_APIGATEWAY_ROOT_V2 = BK_PAAS_HOST + ESB_PREFIX_V2 + "gse/"
ESB_APIGATEWAY_ROOT_V2 = BK_PAAS_HOST + ESB_PREFIX_V2 + "esb/"
JOB_APIGATEWAY_ROOT_V2 = BK_PAAS_HOST + ESB_PREFIX_V2 + "job/"
JOB_APIGATEWAY_ROOT_V3 = BK_PAAS_HOST + ESB_PREFIX_V2 + "jobv3/"

MONITOR_APIGATEWAY_ROOT = BK_PAAS_HOST + ESB_PREFIX_V2 + "monitor_v3/"


# 数据平台模块域名
META_APIGATEWAY_ROOT = BK_PAAS_HOST + ESB_PREFIX + "data/v3/meta/"
DATAQUERY_APIGATEWAY_ROOT = BK_PAAS_HOST + ESB_PREFIX + "data/v3/dataquery/"
DATABUS_APIGATEWAY_ROOT = BK_PAAS_HOST + ESB_PREFIX + "data/v3/databus/"
AUTH_APIGATEWAY_ROOT = BK_PAAS_HOST + ESB_PREFIX + "data/v3/auth/"
STOREKIT_APIGATEWAY_ROOT = BK_PAAS_HOST + ESB_PREFIX + "data/v3/storekit/"
ACCESS_APIGATEWAY_ROOT = BK_PAAS_HOST + ESB_PREFIX + "data/v3/access/"


# 信息推送
CMSI_API_ROOT = BK_PAAS_HOST + ESB_PREFIX + "cmsi/"

# 节点管理
BK_NODE_APIGATEWAY_ROOT = BK_PAAS_HOST + ESB_PREFIX_V2 + "nodeman/"

# LOG SEARCH
LOG_SEARCH_APIGATEWAY_ROOT = BK_PAAS_HOST + ESB_PREFIX_V2 + "bk_log/"
