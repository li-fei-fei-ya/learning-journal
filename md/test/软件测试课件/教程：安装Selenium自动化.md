# 教程：安装Selenium自动化

教程：安装Selenium⾃动化
💡前提：
java版本最低要求为8
电脑⾄少已安装⼀种浏览器，如：Chrome（推荐）、Edge、Firefox、IE、Safari（课堂以
Chrome浏览器演⽰）
提⽰：浏览器必须为官⽹下载的正版浏览器，根据以往经验，存在部分同学电脑安装的浏览器为盗版，导致⽆法执⾏⾃动化

### 1.打开intellij idea，创建Maven项⽬



### 2.添加依赖

<dependencies>
<dependency>
<groupId>org.seleniumhq.selenium</groupId>
<artifactId>selenium-java</artifactId>
<version> 4.0.0</version>
</dependency>
<dependency>
<groupId>io.github.bonigarcia</groupId>
<artifactId>webdrivermanager</artifactId>
<version> 5.8.0</version>
<scope>test</scope>
</dependency>
</dependencies>1
2
3
4
5
6
7
8
9
10
11
12

### 133.在Test路径下创建⾃动化⽂件

1）项⽬结构

2）代码
firstTest.java
public class firstTest {
void searchTest ()
{
//使⽤插件管理⼯具webdrivermanager
WebDriverManager. chromedriver ().setup();
//添加浏览器配置
ChromeOptions options = new ChromeOptions ();
//1)允许任何来源的远程连接
options.addArguments( "--remote-allow-origins=*" );
//创建浏览器驱动对象
ChromeDriver driver = new ChromeDriver (options);
//访问百度⽹⻚，搜索“ ⽐特科技”
driver.get( "https://www.baidu.com" );
driver.findElement(By. cssSelector ("#kw")).sendKeys( "⽐特科技");
driver.findElement(By. cssSelector ("#su")).click();
//退出
driver.quit();
}
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21runTest.java
public class runTest {
public static void main(String[] args) {
firstTest test = new firstTest ();
test.searchTest();1
2
3
4

}
}5
6

### 4.运⾏⾃动化点击运⾏，程序将⾃动实现百度搜索全过程。
