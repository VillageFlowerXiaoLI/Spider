#数据库格式文档
##爬虫格式文档
|字段名称|字段类型|内容说明|
|----|----|----|
|source_url|text(P_K)|游记url
|source_type|text|游记源网站类型 (ctrip/tuniu/qunar)
|title|text|游记标题
|content|text|游记正文，若有分段落则以 _ 连接
|img_urls|text|游记正文图片url, _ 连接
