# BOSS直聘爬取

主要获取的数据

**工作标题，工作链接，工作地点，薪资，年限，学历，公司名，公司链接，公司行业，融资情况，人数，工作标签，公司福利**



## 思路

### 获取城市代码数据

get_citydata()

BOSS直聘自带的查询json

https://www.zhipin.com/wapi/zpgeek/common/data/citysites.json



### 获取网页页面

查询职位链接如下：城市代码，职位名称，页数

'https://www.zhipin.com/c{0}/?query={1}&page={2}'.format(citycode[city], urllib.parse.quote(job), pages)

主要是获取到**job-list**这个分类下的数据



### 解析页面：

parse_html()

主要通过**beautifulsoup**解析job-list下的数据，通过css选择器选择对应的元素并进行记录

一些比较复杂的数据，通过**re正则**提取响应数据



### 反爬：

init_browser()：应用扫码登陆并记录cookies以供获取网页页面时使用

