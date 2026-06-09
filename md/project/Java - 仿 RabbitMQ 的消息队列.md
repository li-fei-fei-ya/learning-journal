# Java - 仿 RabbitMQ 的消息队列

Java -仿RabbitMQ 的消息队列版权说明本“⽐特就业课”项⽬（以下简称“本项⽬”）的所有内容，包括但不限于⽂字、图⽚、⾳频、视频、软件、程序、数据库、设计、布局、界⾯等，均由本项⽬的开发者或授权⽅拥有版权。我们⿎励个⼈学习者使⽤本项⽬进⾏学习和研究。在遵守相关法律法规的前提下，个⼈学习者可以下载、浏览、学习本项⽬的内容，并为了个⼈学习、研究或教学⽬的⽽使⽤其中的材料。但请注意，未经我们明确授权，个⼈学习者不得将本项⽬的内容⽤于任何商业⽬的，包括但不限于销售、转让、许可或以其他⽅式从中获利。此外，个⼈学习者也不得擅⾃修改、复制、传播、展⽰、表演或制作本项⽬内容的衍⽣作品。任何未经授权的使⽤均属侵权⾏为，我们将依法追究法律责任。如果您希望以其他⽅式使⽤本项⽬的内容，包括但不限于引⽤、转载、摘录、改编等，请事先与我们取得联系，获取书⾯授权。感谢您对“⽐特就业课”项⽬的关注与⽀持，我们将持续努⼒，为您提供更好的学习体验。特此说明。⽐特就业课版权所有⽅
对⽐特项⽬感兴趣，可以联系这个微信。
代码&板书链接
https://gitee.com/HGtz2222/bitproject/tree/master/%E6%A8%A1%E6%8B%9F%E5%AE%9E%E
7%8E%B0%E6%B6%88%E6%81%AF%E9%98%9F%E5%88%97

⼀.消息队列背景知识曾经我们学习过阻塞队列(BlockingQueue) ,我们说,阻塞队列最⼤的⽤途,就是⽤来实现⽣产者消费者模型.
⽣产者消费者模型,存在诸多好处 ,是后端开发的常⽤编程⽅式.
•解耦合
•削峰填⾕
在实际的后端开发中,尤其是分布式系统⾥,跨主机之间使⽤⽣产者消费者模型,也是⾮常普遍的需求.
因此,我们通常会把阻塞队列,封装成⼀个独⽴的服务器程序,并且赋予其更丰富的功能.
这样的程序我们就称为消息队列(Message Queue, MQ)
市⾯上成熟的消息队列⾮常多.
•RabbitMQ
•Kafka
•RocketMQ
•ActiveMQ
•......
其中,RabbitMQ 是⼀个⾮常知名,功能强⼤,⼴泛使⽤的消息队列.
咱们就仿照RabbitMQ, 模拟实现⼀个简单的消息队列.
⼆.需求分析核⼼概念
•⽣产者(Producer)
•消费者(Consumer)
•中间⼈(Broker)
•发布(Publish)
•订阅(Subscribe)

⼀个⽣产者,⼀个消费者
N个⽣产者,N个消费者其中,Broker 是最核⼼的部分.负责消息的存储和转发.
在Broker 中,⼜存在以下概念.
•虚拟机(VirtualHost): 类似于MySQL 的"database", 是⼀个逻辑上的集合.⼀个BrokerServer 上可以存在多个VirtualHost.
•交换机(Exchange): ⽣产者把消息先发送到Broker 的Exchange 上.再根据不同的规则,把消息转发给不同的Queue.
•队列(Queue): 真正⽤来存储消息的部分.每个消费者决定⾃⼰从哪个Queue 上读取消息.
•绑定(Binding): Exchange 和Queue 之间的关联关系.Exchange 和Queue 可以理解成"多对多"关系.使⽤⼀个关联表就可以把这两个概念联系起来.
•消息(Message): 传递的内容.
所谓的Exchange 和Queue 可以理解成"多对多"关系,和数据库中的"多对多"⼀样.意思是:
⼀个Exchange 可以绑定多个Queue (可以向多个Queue 中转发消息).
⼀个Queue 也可以被多个Exchange 绑定(⼀个Queue 中的消息可以来⾃于多个Exchange).

这些概念,既需要在内存中存储,也需要在硬盘上存储.
•内存存储:⽅便使⽤.
•硬盘存储:重启数据不丢失.
核⼼API
对于Broker 来说,要实现以下核⼼API.通过这些API来实现消息队列的基本功能.

### 1.创建队列(queueDeclare)


### 2.销毁队列(queueDelete)


### 3.创建交换机(exchangeDeclare)


### 4.销毁交换机(exchangeDelete)


### 5.创建绑定(queueBind)


### 6.解除绑定(queueUnbind)


### 7.发布消息(basicPublish)


### 8.订阅消息(basicConsume)


### 9.确认消息(basicAck)

另⼀⽅⾯,Producer 和Consumer 则通过⽹络的⽅式,远程调⽤这些API,实现⽣产者消费者模型.
关于VirtualHost
对于RabbitMQ 来说,VirtualHost 也是可以随意创建删除的.

此处咱们暂时不做这部分功能(实现起来也⽐较简单,咱们的代码中会完成部分和虚拟主机相关的结构设计.⼤家可以⾃⾏完成管理逻辑).
交换机类型(Exchange Type)
对于RabbitMQ 来说,主要⽀持四种交换机类型.
•Direct
•Fanout
•Topic
•Header
其中Header 这种⽅式⽐较复杂,⽐较少⻅.常⽤的是前三种交换机类型.咱们此处也主要实现这三种.
•Direct: ⽣产者发送消息时,直接指定被该交换机绑定的队列名.
•Fanout: ⽣产者发送的消息会被复制到该交换机的所有队列中.
•Topic: 绑定队列到交换机上时,指定⼀个字符串为bindingKey. 发送消息指定⼀个字符串为
routingKey. 当routingKey 和bindingKey 满⾜⼀定的匹配条件的时候,则把消息投递到指定队列.
这三种操作就像给qq群发红包.
•Direct 是发⼀个专属红包,只有指定的⼈能领.
•Fanout 是使⽤了魔法,发⼀个10块钱红包,群⾥的每个⼈都能领10块钱.
•Topic 是发⼀个画图红包,发10块钱红包,同时出个题,得画的像的⼈,才能领.也是每个领到的⼈
都能领10块钱.
持久化
Exchange, Queue, Binding, Message 都有持久化需求.
当程序重启/主机重启,保证上述内容不丢失.
⽹络通信
⽣产者和消费者都是客⼾端程序,broker 则是作为服务器.通过⽹络进⾏通信.
在⽹络通信的过程中,客⼾端部分要提供对应的api,来实现对服务器的操作.

### 1.创建Connection



### 2.关闭Connection


### 3.创建Channel


### 4.关闭Channel


### 5.创建队列(queueDeclare)


### 6.销毁队列(queueDelete)


### 7.创建交换机(exchangeDeclare)


### 8.销毁交换机(exchangeDelete)


### 9.创建绑定(queueBind)


### 10.解除绑定(queueUnbind)


### 11.发布消息(basicPublish)


### 12.订阅消息(basicConsume)


### 13.确认消息(basicAck)

可以看到,在broker 的基础上,客⼾端还要增加Connection 操作和Channel 操作.
Connection 对应⼀个TCP连接.
Channel 则是Connection 中的逻辑通道.
⼀个Connection 中可以包含多个Channel.
Channel 和Channel 之间的数据是独⽴的.不会相互⼲扰.
这样的设定主要是为了能够更好的复⽤TCP连接,达到⻓连接的效果,避免频繁的创建关闭TCP连接.
Connection 可以理解成⼀根⽹线.Channel 则是⽹线⾥具体的线缆.
消息应答被消费的消息,需要进⾏应答.

应答模式分成两种.
•⾃动应答:消费者只要消费了消息,就算应答完毕了.Broker 直接删除这个消息.
•⼿动应答:消费者⼿动调⽤应答接⼝,Broker 收到应答请求之后,才真正删除这个消息.
⼿动应答的⽬的,是为了保证消息确实被消费者处理成功了.在⼀些对于数据可靠性要求⾼的场景,⽐
较常⻅.
三.模块划分

可以看到,像交换机,队列,绑定,消息,这⼏个核⼼概念在内存和硬盘中都是存储了的.
其中内存为主,是⽤来实现消息转发的关键;硬盘为辅,主要是保证服务器重启之后,之前的信息都可以正常保持.
四.项⽬创建创建SpringBoot 项⽬.
使⽤SpringBoot 2系列版本,Java 8.

依赖引⼊Spring Web 和MyBatis.
五.创建核⼼类创建包mqserver.core
创建Exchange
public class Exchange {
private String name;
private ExchangeType type = ExchangeType.DIRECT;
private boolean durable = false;
private boolean autoDelete = false;
private Map<String, Object> arguments = new HashMap<>();

// 省略 getter setter
}1
2
3
4
5
6
7
8
9
public enum ExchangeType {
DIRECT( 0),
FANOUT( 1),
TOPIC( 2);
private final int type;
private ExchangeType (int type) {
this.type = type;
}
public int getType() {
return this.type;
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
•name :交换机的名字.相当于交换机的⾝份标识.
•type :交换机的类型.三种取值,DIRECT, FANOUT, TOPIC.
•durable :交换机是否要持久化存储.true为持久化,false 不持久化.
•autoDelete :使⽤完毕后是否⾃动删除.预留字段,暂时未使⽤.
•arguments :交换机的其他参数属性.预留字段,暂时未使⽤.

RabbitMQ 中的交换机,⽀持autoDelete 和arguments ,咱们此处为了简单,暂时没有实现对应功能,只是预留了字段,同学们可以尝试⾃⼰完成.
创建MSGQueue
public class MSGQueue {
private String name;
private boolean durable;
private boolean exclusive;
private boolean autoDelete;
private Map<String, Object> arguments = new HashMap<>();
// 省略 getter setter
}1
2
3
4
5
6
7
8
9
类名叫做MSGQueue, ⽽不是Queue, 是为了防⽌和标准库中的Queue 混淆.
•name :队列的名字.相当于队列的⾝份标识.
•durable :交换机是否要持久化存储.true为持久化,false 不持久化.
•exclusive :独占(排他),队列只能被⼀个消费者使⽤.
•autoDelete :使⽤完毕后是否⾃动删除.预留字段,暂时未使⽤.
•arguments :交换机的其他参数属性.预留字段,暂时未使⽤.
创建Binding
public class Binding {
private String exchangeName;
private String queueName;
private String bindingKey;
// 省略 getter setter
}1
2
3
4
5
6
7
•exchangeName 交换机名字
•queueName 队列名字
•bindingKey 只在交换机类型为TOPIC 时才有效.⽤于和消息中的routingKey 进⾏匹配.

创建Message
public class Message implements Serializable {
private BasicProperties basicProperties = new BasicProperties ();
private byte[] body;
// 消息在⽂件中对应的 offset 的范围, [offsetBeg, offsetEnd)
// 从这个范围取出的 byte[] 正好可以反序列化成⼀个 Message 对象.
// offsetBeg 前⾯的 4 个字节是消息的⻓度
private transient long offsetBeg = 0;
private transient long offsetEnd = 0;
// 消息在⽂件中是否有效. 0x0 表⽰⽆效, 0x1 表⽰有效
private byte isValid = 0x1;
// 创建新的消息, 同时给该消息分配⼀个新的 messageId
// routingKey 以参数的为准. 会覆盖掉 basicProperties 中的 routingKey
public static Message createMessageWithId (String routingKey,
BasicProperties basicProperties, byte[] body) {
Message message = new Message();
if (basicProperties != null) {
message.basicProperties = basicProperties;
}
message.basicProperties.setMessageId( "M-" +
UUID.randomUUID().toString());
message.basicProperties.setRoutingKey(routingKey);
message.body = body;
return message;
}

// 省略 getter setter
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
21
22
23
24
25
26
27
28
public class BasicProperties implements Serializable {
// 消息的唯⼀ id. 使⽤ uuid 表⽰.
private String messageId;
private String routingKey;
// 1 表⽰消息⾮持久化. 2 表⽰消息持久化
private int deliveryMode = 1;

// 省略 getter setter
}1
2
3
4
5
6
7
8
9

•Message 需要实现Serializable 接⼝.后续需要把Message 写⼊⽂件以及进⾏⽹络传输.
•basicProperties 是消息的属性信息.body 是消息体.
•offsetBeg 和offsetEnd 表⽰消息在消息⽂件中所在的起始位置和结束位置.这⼀块具体的设计后⾯再详细介绍.使⽤transient 关键字避免属性被序列化.
•isValid ⽤来表⽰消息在⽂件中是否有效.这⼀块具体的设计后⾯再详细介绍.
•createMessageWithId 相当于⼀个⼯⼚⽅法,⽤来创建⼀个Message 实例.messageId 通过
UUID 的⽅式⽣成.
六.数据库设计对于Exchange, MSGQueue, Binding, 我们使⽤数据库进⾏持久化保存.
此处我们使⽤的数据库是SQLite, 是⼀个更轻量的数据库.
SQLite 只是⼀个动态库(当然,官⽅也提供了可执⾏程序exe), 我们在Java 中直接引⼊SQLite 依赖,即可直接使⽤,不必安装其他的软件.
配置sqlite
引⼊pom.xml 依赖
<dependency >
<groupId>org.xerial</ groupId>
<artifactId >sqlite-jdbc</ artifactId >
<version>3.41.0.1</ version>
</dependency >1
2
3
4
5
配置数据源application.yml
spring:
datasource:
url: jdbc:sqlite:./data/meta.db
username:
password:
driver-class-name: org.sqlite.JDBC
mybatis:
mapper-locations: classpath:mapper/**Mapper.xml1
2
3
4
5
6
7
8
9

Username 和password 空着即可.
此处我们约定,把数据库⽂件放到./data/meta.db 中.
SQLite 只是把数据单纯的存储到⼀个⽂件中.⾮常简单⽅便.
实现创建表
@Mapper
public interface MetaMapper {
void createUserTable ();
void createExchangeTable ();
void createQueueTable ();
void createBindingTable ();
}1
2
3
4
5
6
7
本⾝MyBatis 针对MySQL /Oracle ⽀持执⾏多个SQL语句的,但是针对SQLite 是不⽀持的,只能写成多个⽅法.
<update id="createExchangeTable" >
create table if not exists exchange (
name varchar(50) primary key,
type int, -- 0 表⽰ direct, 1 表⽰ fanout, 2 表⽰
topic
durable boolean, -- false 表⽰不持久化, true 表⽰持久化.
autoDelete boolean, -- false 表⽰不⾃动删除, true 表⽰⾃动删除.
arguments varchar(1024) -- 创建交换机指定的参数
);
</update>
<update id="createQueueTable" >
create table if not exists queue (
name varchar(50) primary key,
durable boolean, -- false 表⽰不持久化, true 表⽰持久化.
autoDelete boolean, -- false 表⽰不⾃动删除, true 表⽰⾃动删除.
arguments varchar(1024) -- 创建交换机指定的参数
);
</update>
<update id="createBindingTable" >
create table if not exists binding (1
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
21

exchangeName varchar(50),
queueName varchar(50),
bindingKey varchar(256)
);
</update>22
23
24
25
26
实现数据库基本操作给mapper.MetaMapper 中添加
void insertExchange (Exchange exchange);
void deleteExchange (String exchangeName);
void insertQueue (MSGQueue msgQueue);
void deleteQueue (String queueName);
void insertBinding (Binding binding);
void deleteBinding (Binding binding);1
2
3
4
5
6
给MetaMapper 中添加
<insert id="insertExchange"
parameterType ="com.example.java_message_queue.mqserver.core.Exchange" >
insert into exchange values(#{name}, #{type}, #{durable}, #{autoDelete}, #
{arguments});
</insert>
<delete id="deleteExchange" parameterType ="java.lang.String" >
delete from exchange where name = #{exchangeName};
</delete>
<insert id="insertQueue"
parameterType ="com.example.java_message_queue.mqserver.core.MSGQueue" >
insert into queue values(#{name}, #{durable}, #{autoDelete}, #{arguments});
</insert>
<delete id="deleteQueue" parameterType ="java.lang.String" >
delete from queue where name = #{queueName};
</delete>
<insert id="insertBinding"
parameterType ="com.example.java_message_queue.mqserver.core.Binding" >1
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

insert into binding values(#{exchangeName}, #{queueName}, #{bindingKey});
</insert>
<delete id="deleteBinding"
parameterType ="com.example.java_message_queue.mqserver.core.Binding" >
delete from binding where exchangeName = #{exchangeName} and queueName = #
{queueName};
</delete>18
19
20
21
22
23
实现DataBaseManager
mqserver.datacenter.DataBaseManager
1)创建DataBaseManager 类通过这个类来封装针对数据库的操作.
public class DataBaseManager {
// 由于 DataBaseManager 不是⼀个 Bean
// 需要⼿动来获取实例
private MetaMapper metaMapper;

public void init() {
this.metaMapper =
JavaMessageQueueApplication.ac.getBean(MetaMapper.class);

// 构造数据库
if (!checkDBExists()) {
// 1. 读取 sql ⽂件中的内容, 并创建表
createTable();
// 2. 插⼊默认数据
createDefaultData();
System.out.println( "[DataBaseManager] 数据库初始化完成!");
} else {
System.out.println( "[DataBaseManager] 数据库已经存在!");
}
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
如果数据库⽂件存在,则不必建库建表了.

针对JavaMessageQueueApplication, 需要新增⼀个ac属性.并初始化
@SpringBootApplication
public class JavaMessageQueueApplication {
public static ConfigurableApplicationContext ac;
public static void main(String[] args) throws IOException {
ac = SpringApplication.run(JavaMessageQueueApplication.class);
}
}1
2
3
4
5
6
7
8
2)实现checkDBExists
private boolean checkDBExists () {
File file = new File("./meta.db" );
if (file.exists()) {
return true;
}
return false;
}1
2
3
4
5
6
7
3)实现createTable
// 创建数据表
private void createTable () {
metaMapper.createExchangeTable();
metaMapper.createQueueTable();
metaMapper.createBindingTable();
System.out.println( "[DataBaseManager] 创建表完成!");
}1
2
3
4
5
6
7
4)实现createDefaultData
// 创建表中的默认数据 1

private void createDefaultData () {
// 构造默认交换机
Exchange exchange = new Exchange ();
exchange.setName( "");
exchange.setType(ExchangeType.DIRECT);
exchange.setDurable( true);
exchange.setAutoDelete( false);
metaMapper.insertExchange(exchange);
System.out.println( "[DataBaseManager] 创建初始数据完成!");
}2
3
4
5
6
7
8
9
10
11
默认数据主要是创建⼀个默认的交换机.这个默认交换机没有名字,并且是直接交换机.
5)封装其他数据库操作
public void insertExchange (Exchange exchange) {
metaMapper.insertExchange(exchange);
}
public void deleteExchange (String exchangeName) {
metaMapper.deleteExchange(exchangeName);
}
public List<Exchange> selectAllExchanges () {
return metaMapper.selectAllExchanges();
}
public void insertQueue (MSGQueue queue) {
metaMapper.insertQueue(queue);
}
public void deleteQueue (String queueName) {
metaMapper.deleteQueue(queueName);
}
public List<MSGQueue> selectAllQueues () {
return metaMapper.selectAllQueues();
}
public void insertBinding (Binding binding) {
metaMapper.insertBinding(binding);
}
public void deleteBinding (Binding binding) {1
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
21
22
23
24
25
26
27
28
29

metaMapper.deleteBinding(binding);
}
public List<Binding> selectAllBindings () {
return metaMapper.selectAllBindings();
}30
31
32
33
34
35
测试DataBaseManager
使⽤Spring ⾃带的单元测试,针对上述代码进⾏测试验证.
在test⽬录中,创建DataBaseManagerTests
1)准备⼯作
@SpringBootTest
public class DataBaseManagerTests {
private static DataBaseManager dataBaseManager = new DataBaseManager ();
@BeforeAll
public static void setupAll () throws IOException {
// 初始情况下, 先统⼀清除数据库
dataBaseManager.deleteDB();
}
@BeforeEach
public void setUp() throws IOException {
// 每次运⾏⼀个⽤例, 都重置数据库. 防⽌⽤例之间的数据相互⼲扰.
// 需要初始化 ac 对象
JavaMessageQueueApplication.ac =
SpringApplication.run(JavaMessageQueueApplication.class);
// 再初始化数据库
dataBaseManager.init();
}
@AfterEach
public void tearDown () throws IOException {
// 需要关闭 ac 对象
JavaMessageQueueApplication.ac.close();
// 然后再删除数据库
dataBaseManager.deleteDB();
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
21
22
23
24
25
26

}27
•@SpringBootTest 注解表⽰该类是⼀个测试类.
•@BeforeAll 在所有测试执⾏之前执⾏.此处先删除之前的数据库,避免⼲扰.
•@BeforeEach 每个测试⽤例之前执⾏.⼀般⽤来做准备⼯作.此处进⾏数据库初始化,以及针对
Spring 服务的初始化.
•@AfterEach 每个测试⽤例之后执⾏.⼀般⽤来做收尾⼯作.此处需要先关闭Spring 服务,再删除数据库.
由于Spring 服务启动的时候,会和数据库建⽴连接(通过MyBatis). 因此需要先关闭服务,才能删除数据库,否则会删除失败(Spring 服务会持有数据库⽂件的访问权限).
2)编写测试⽤例
•@Test 注解表⽰⼀个测试⽤例.
•Assertions 是断⾔,⽤来断定执⾏结果.
•每个⽤例执⾏之前,都会⾃动调⽤到setUp, 每次⽤例执⾏结束之后,都会⾃动调⽤tearDown
•要确保每个⽤例的执⾏都是"clean" 的,也就是该⽤例不会被上个⽤例⼲扰到.
@Test
public void testInitTable () throws IOException {
List<Exchange> exchangeList = dataBaseManager.selectAllExchanges();
List<MSGQueue> queueList = dataBaseManager.selectAllQueues();
List<Binding> bindingList = dataBaseManager.selectAllBindings();
Assertions.assertEquals( 1, exchangeList.size());
Assertions.assertEquals( "", exchangeList.get( 0).getName());
Assertions.assertEquals(ExchangeType.DIRECT,
exchangeList.get( 0).getType());
Assertions.assertEquals( 0, queueList.size());
Assertions.assertEquals( 0, bindingList.size());
}
private Exchange createTestExchange (String exchangeName) {
Exchange exchange = new Exchange ();
exchange.setName(exchangeName);
exchange.setType(ExchangeType.FANOUT);
exchange.setAutoDelete( true);
exchange.setDurable( true);
HashMap<String, Object> arguments = new HashMap<>();
arguments.put( "aaa", "111");1
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
21

arguments.put( "bbb", "222");
exchange.setArguments(arguments);
return exchange;
}
@Test
public void testInsertExchange () {
Exchange exchange = createTestExchange( "test");
dataBaseManager.insertExchange(exchange);
List<Exchange> exchangeList = dataBaseManager.selectAllExchanges();
Assertions.assertEquals( 2, exchangeList.size());
Assertions.assertEquals( "test", exchangeList.get( 1).getName());
Assertions.assertEquals(ExchangeType.FANOUT,
exchangeList.get( 1).getType());
Assertions.assertEquals( true, exchangeList.get( 1).isAutoDelete());
Assertions.assertEquals( true, exchangeList.get( 1).isDurable());
Assertions.assertEquals( "111", exchangeList.get( 1).getArgument( "aaa"));
Assertions.assertEquals( "222", exchangeList.get( 1).getArgument( "bbb"));
}
@Test
public void testDeleteExchange () {
Exchange exchange = createTestExchange( "test");
dataBaseManager.insertExchange(exchange);
List<Exchange> exchangeList = dataBaseManager.selectAllExchanges();
Assertions.assertEquals( 2, exchangeList.size());
Assertions.assertEquals( "test", exchangeList.get( 1).getName());
dataBaseManager.deleteExchange( "test");
exchangeList = dataBaseManager.selectAllExchanges();
Assertions.assertEquals( 1, exchangeList.size());
Assertions.assertEquals( "", exchangeList.get( 0).getName());
}
private MSGQueue createTestQueue (String queueName) {
MSGQueue queue = new MSGQueue ();
queue.setName(queueName);
queue.setDurable( true);
queue.setAutoDelete( true);
queue.setExclusive( true);
HashMap<String, Object> hashMap = new HashMap<>();
hashMap.put( "aaa", "111");
hashMap.put( "bbb", "222");
queue.setArguments(hashMap);
return queue;
}22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67

@Test
public void testInsertQueue () {
MSGQueue queue = createTestQueue( "test");
dataBaseManager.insertQueue(queue);
List<MSGQueue> queueList = dataBaseManager.selectAllQueues();
Assertions.assertEquals( 1, queueList.size());
Assertions.assertEquals( "test", queueList.get( 0).getName());
Assertions.assertEquals( true, queueList.get( 0).isDurable());
Assertions.assertEquals( true, queueList.get( 0).isAutoDelete());
Assertions.assertEquals( true, queueList.get( 0).isExclusive());
Assertions.assertEquals( "111", queueList.get( 0).getArgument( "aaa"));
Assertions.assertEquals( "222", queueList.get( 0).getArgument( "bbb"));
}
@Test
public void testDeleteQueue () {
MSGQueue queue = createTestQueue( "test");
dataBaseManager.insertQueue(queue);
List<MSGQueue> queueList = dataBaseManager.selectAllQueues();
Assertions.assertEquals( 1, queueList.size());
Assertions.assertEquals( "test", queueList.get( 0).getName());
dataBaseManager.deleteQueue( "test");
queueList = dataBaseManager.selectAllQueues();
Assertions.assertEquals( 0, queueList.size());
}
@Test
public void testInsertBinding () {
Binding binding = new Binding();
binding.setQueueName( "testQueue" );
binding.setExchangeName( "testExchange" );
binding.setBindingKey( "testBindingKey" );
dataBaseManager.insertBinding(binding);
List<Binding> bindingList = dataBaseManager.selectAllBindings();
Assertions.assertEquals( 1, bindingList.size());
Assertions.assertEquals( "testQueue" , bindingList.get( 0).getQueueName());
Assertions.assertEquals( "testExchange" ,
bindingList.get( 0).getExchangeName());
Assertions.assertEquals( "testBindingKey" ,
bindingList.get( 0).getBindingKey());
}
@Test
public void testDeleteBinding () {
Binding binding = new Binding();68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112

binding.setQueueName( "testQueue" );
binding.setExchangeName( "testExchange" );
binding.setBindingKey( "testBindingKey" );
dataBaseManager.insertBinding(binding);
List<Binding> bindingList = dataBaseManager.selectAllBindings();
Assertions.assertEquals( 1, bindingList.size());
dataBaseManager.deleteBinding(binding);
bindingList = dataBaseManager.selectAllBindings();
Assertions.assertEquals( 0, bindingList.size());
}113
114
115
116
117
118
119
120
121
122
123
124
125
七.消息存储设计设计思路消息需要在硬盘上存储.但是并不直接放到数据库中,⽽是直接使⽤⽂件存储.
原因如下:

### 1.对于消息的操作并不需要复杂的增删改查.


### 2.对于⽂件的操作效率⽐数据库会⾼很多.

主流MQ的实现(包括RabbitMQ), 都是把消息存储在⽂件中,⽽不是数据库中.
我们给每个队列分配⼀个⽬录.⽬录的名字为data +队列名.形如./data/testQueue
该⽬录中包含两个固定名字的⽂件.
•queue_data.txt 消息数据⽂件,⽤来保存消息内容.
•queue_stat.txt 消息统计⽂件,⽤来保存消息统计信息.
queue_data.txt ⽂件格式:
使⽤⼆进制⽅式存储.
每个消息分成两个部分:
•前四个字节,表⽰Message 对象的⻓度(字节数)
•后⾯若⼲字节,表⽰Message 内容.
•消息和消息之间⾸尾相连.

每个Message 基于Java 标准库的ObjectInputStream /ObjectOutputStream 序列化.
Message 对象中的offsetBeg 和offsetEnd 正是⽤来描述每个消息体所在的位置.
queue_stat.txt ⽂件格式:
使⽤⽂本⽅式存储.
⽂件中只包含⼀⾏,⾥⾯包含两列(都是整数),使⽤\t分割.
第⼀列表⽰当前总的消息数⽬.第⼆列表⽰有效消息数⽬.
形如:
2000\t15001
创建MessageFileManager 类创建mqserver.database.MessageFileManager
public class MessageFileManager {
// 表⽰消息的统计信息
static public class Stat {
public int totalCount;
public int validCount;
}
public void init() {
// 当前这⾥不需要做任何⼯作.
}
// 队列⽬录
private String getQueueDir (String queueName) {
return "./data/" + queueName;
}
// 队列数据⽂件 1
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

// 这个⽂件来存储队列的真实数据
private String getQueueDataPath (String queueName) {
return getQueueDir(queueName) + "/queue_data.txt" ;
}
// 队列统计⽂件
// 这个⽂件⽤来存储队列中的统计信息.
// 包含⼀⾏, 两个列使⽤ \t 分割, 分别是总数据, 和⽆效数据.
private String getQueueStatPath (String queueName) {
return getQueueDir(queueName) + "/queue_stat.txt" ;
}
}18
19
20
21
22
23
24
25
26
27
28
29
•内部包含⼀个Stat类,⽤来表⽰消息统计⽂件的内容.
•getQueueDir, getQueueDataPath, getQueueStatPath ⽤来表⽰这⼏个⽂件所在位置.
实现统计⽂件读写这是后续操作的⼀项准备⼯作.
// 从统计⽂件中读取结果
private Stat readStat (String queueName) {
Stat stat = new Stat();
try (InputStream inputStream = new
FileInputStream (getQueueStatPath(queueName))) {
Scanner scanner = new Scanner(inputStream);
stat.totalCount = scanner.nextInt();
stat.validCount = scanner.nextInt();
return stat;
} catch (IOException e) {
e.printStackTrace();
}
return null;
}
// 向统计⽂件中写⼊结果
private void writeStat (String queueName, Stat stat) {
try (OutputStream outputStream = new
FileOutputStream (getQueueStatPath(queueName))) {
PrintWriter printWriter = new PrintWriter (outputStream);
printWriter.write(stat.totalCount + "\t" + stat.validCount);
printWriter.flush();
} catch (IOException e) {1
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
21

e.printStackTrace();
}
}22
23
24
直接使⽤Scanner 和PrintWriter 进⾏读写即可.
实现创建队列⽬录每个队列都有⾃⼰的⽬录和配套的⽂件.通过下列⽅法把⽬录和⽂件先准备好.
public void createQueueFiles (String queueName) throws IOException {
// 1. 创建⽬录指定队列的⽬录
File baseDir = new File(getQueueDir(queueName));
if (!baseDir.exists()) {
boolean ok = baseDir.mkdirs();
if (!ok) {
throw new IOException ("创建⽬录失败! baseDir=" +
baseDir.getAbsolutePath());
}
}
// 2. 创建队列数据⽂件
File queueDataFile = new File(getQueueDataPath(queueName));
if (!queueDataFile.exists()) {
boolean ok = queueDataFile.createNewFile();
if (!ok) {
throw new IOException ("创建⽂件失败! queueDataFile=" +
queueDataFile.getAbsolutePath());
}
}
// 3. 创建队列统计⽂件
File queueStatFile = new File(getQueueStatPath(queueName));
if (!queueStatFile.exists()) {
boolean ok = queueStatFile.createNewFile();
if (!ok) {
throw new IOException ("创建⽂件失败! queueStatFile=" +
queueStatFile.getAbsolutePath());
}
}
// 4. 给队列统计⽂件写⼊初始数据
Stat stat = new Stat();
stat.totalCount = 0;
stat.validCount = 0;
writeStat(queueName, stat);
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
21
22
23
24
25
26
27
28
29
30
31

把上述约定的⽂件都创建出来,并对消息统计⽂件进⾏初始化.
初始化0\t0 这样的初始值.
实现删除队列⽬录如果队列需要删除,则队列对应的⽬录/⽂件也需要删除.
public void destroyQueueFiles (String queueName) throws IOException {
// 1. 先删除⽬录中的⽂件
File queueDataFile = new File(getQueueDataPath(queueName));
boolean ok1 = queueDataFile.delete();
File queueStatFile = new File(getQueueStatPath(queueName));
boolean ok2 = queueStatFile.delete();
// 2. 再删除⽬录. delete 要求必须是空⽬录才能删除.
File baseDir = new File(getQueueDir(queueName));
boolean ok3 = baseDir.delete();
if (!ok1 || !ok2 || !ok3) {
throw new IOException ("删除队列⽬录失败! baseDir=" +
baseDir.getAbsolutePath());
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
注意:File类的delete ⽅法只能删除空⽬录.因此需要先把内部的⽂件先删除掉.
检查队列⽂件是否存在判定该队列的消息⽂件和统计⽂件是否存在.⼀旦出现缺失,则不能进⾏后续⼯作.
private boolean checkFilesExists (String queueName) {
File queueData = new File(getQueueDataPath(queueName));
if (!queueData.exists()) {
return false;
}
File queueStat = new File(getQueueStatPath(queueName));
if (!queueStat.exists()) {
return false;
}
return true;
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

实现消息对象序列化/反序列化
Message 对象需要转成⼆进制写⼊⽂件.并且也需要把⽂件中的⼆进制读出来解析成Message 对象.此处针对这⾥的逻辑进⾏封装.
创建common.BinaryTool
public class BinaryTool {
public static Object fromBytes (byte[] data) throws IOException,
ClassNotFoundException {
Object object = null;
ByteArrayInputStream byteArrayInputStream = new
ByteArrayInputStream (data);
try (ObjectInputStream objectInputStream = new
ObjectInputStream (byteArrayInputStream)) {
object = objectInputStream.readObject();
}
return object;
}
public static byte[] toBytes(Object object) throws IOException {
ByteArrayOutputStream byteArrayOutputStream = new
ByteArrayOutputStream ();
try (ObjectOutputStream objectOutputStream = new
ObjectOutputStream (byteArrayOutputStream)) {
objectOutputStream.writeObject(object);
}
return byteArrayOutputStream.toByteArray();
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
•使⽤ByteArrayInputStream /ByteArrayOutputStream 针对byte[] 进⾏封装,⽅便后续操作.(这两个流对象是纯内存的,不需要进⾏close).
•使⽤ObjectInputStream /ObjectOutputStream 进⾏序列化/反序列化操作.通过内部的
readObject /writeObject 即可完成对应操作.
•此处涉及到的序列化对象,需要实现Serializable 接⼝.这⼀点咱们的Message 对象已经实现过了.
对于serialVersionUID ,此处咱们暂时不需要.⼤家可以⾃⾏了解serialVersionUID 的⽤途实现写⼊消息⽂件

public void sendMessage (MSGQueue queue, Message message) throws MqException,
IOException {
if (!checkFilesExists(queue.getName())) {
throw new MqException ("[MessageFileManager] 队列匹配的⽂件不存在!
queueName=" + queue.getName());
}
// 1. 先把 message 转成⼆进制
byte[] messageBinary = BinaryTool.toBytes(message);
// 此处的锁对象以队列为维度. 不同队列之间不涉及锁冲突.
synchronized (queue) {
// 2. 先获取到⽂件总⻓度
File queueDataFile = new File(getQueueDataPath(queue.getName()));
message.setOffsetBeg(queueDataFile.length() + 4);
message.setOffsetEnd(queueDataFile.length() + 4 +
messageBinary.length);
// 3. 写⼊消息数据⽂件
try (OutputStream outputStream = new FileOutputStream (queueDataFile,
true)) {
DataOutputStream dataOutputStream = new
DataOutputStream (outputStream);
// 先写⼊消息⻓度
dataOutputStream.writeInt(messageBinary.length);
// 再写⼊消息本体
dataOutputStream.write(messageBinary);
}
// 4. 写⼊消息统计⽂件
Stat stat = readStat(queue.getName());
stat.totalCount += 1;
stat.validCount += 1;
writeStat(queue.getName(), stat);
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
21
22
23
24
25
26
27
•考虑线程安全,按照队列维度进⾏加锁.
•使⽤DataOutputStream 进⾏⼆进制写操作.⽐原⽣OutputStream 要⽅便.
•需要记录Message 对象在⽂件中的偏移量.后续的删除操作依赖这个偏移量定位到消息.offsetBeg
是原有⽂件⼤⼩的基础上,再+4.4个字节是存放消息⼤⼩的空间.(参考上⾯的图).
•写完消息,要同时更新统计信息.
创建common.MqException ,作为⾃定义异常类.后续业务上出现问题,都统⼀抛出这个异常.
实践中创建多个异常类,分别表⽰不同异常种类是更好的做法.此处我们只是偷懒了.

public class MqException extends Exception {
public MqException (String message) {
super(message);
}
}1
2
3
4
5
实现删除消息此处的删除只是"逻辑删除",即把Message 类中的isValid 字段设置为0.
这样删除速度⽐较快.实际的彻底删除,则通过我们⾃⼰实现的GC来解决.
// 把⽂件上的对应消息给删除掉. (标记成⽆效)
public void deleteMessage (MSGQueue queue, Message message) throws IOException,
ClassNotFoundException {
synchronized (queue) {
try (RandomAccessFile randomAccessFile = new
RandomAccessFile (getQueueDataPath(queue.getName()), "rw")) {
// 1. 先从⽂件中读取出 Message 的数据
byte[] bufferSrc = new byte[(int) (message.getOffsetEnd() -
message.getOffsetBeg())];
randomAccessFile.seek(message.getOffsetBeg());
randomAccessFile.read(bufferSrc);
// 2. 转成 Message 对象
Message diskMessage = (Message) BinaryTool.fromBytes(bufferSrc);
// 3. 设置成⽆效.
diskMessage.setIsValid(( byte)0x0);
// 4. 重新写⼊⽂件
byte[] bufferDest = BinaryTool.toBytes(diskMessage);
randomAccessFile.seek(message.getOffsetBeg());
randomAccessFile.write(bufferDest);
}
// 更新统计⽂件
Stat stat = readStat(queue.getName());
if (stat.validCount > 0) {
stat.validCount -= 1;
}
writeStat(queue.getName(), stat);
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
21
22
23
24
25
26
•使⽤RandomAccessFile 来随机访问到⽂件的内容.

•根据Message 中的offsetBeg 和offsetEnd 定位到消息在⽂件中的位置.通过
randomAccessFile.seek 操作⽂件指针偏移过去.再读取.
•读出的结果解析成Message 对象,修改isValid 字段,再重新写回⽂件.注意写的时候要重新设定⽂
件指针的位置.⽂件指针会随着上述的读操作产⽣改变.
•最后,要记得更新统计⽂件,把合法消息-1.
实现消息加载把消息内容从⽂件加载到内存中.这个功能在服务器重启,和垃圾回收的时候都很关键.
// 从消息数据⽂件中读取出所有消息
public LinkedList<Message> loadAllMessageFromQueue (String queueName) throws
MqException, IOException, ClassNotFoundException {
// 记录当前读到的数据在⽂件的 offset
long currentOffset = 0;
LinkedList<Message> messages = new LinkedList <>();
try (InputStream inputStream = new
FileInputStream (getQueueDataPath(queueName))) {
DataInputStream dataInputStream = new DataInputStream (inputStream);
while (true) {
// 读到⽂件末尾, 会触发 EOFException
int messageSize = dataInputStream.readInt();
byte[] buffer = new byte[messageSize];
int actualSize = dataInputStream.read(buffer);
if (messageSize != actualSize) {
throw new MqException ("[MessageFileManager] ⽂件格式错误!
queueName=" + queueName);
}
Message message = (Message) BinaryTool.fromBytes(buffer);
if (message.getIsValid() != 0x1) {
// 被删除的⽆效数据, 直接跳过. 不要忘记更新 currentOffset
currentOffset += 4 + messageSize;
continue ;
}
// 计算该 message 的 offset
message.setOffsetBeg(currentOffset + 4);
message.setOffsetEnd(currentOffset + 4 + messageSize);
// 每个消息, 开头 4 个字节保存的是消息的⻓度. 接下来 [offsetBeg,
offsetEnd) 是消息体
currentOffset += 4 + messageSize;
messages.add(message);
}
} catch (EOFException e) {1
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
21
22
23
24
25
26
27
28
29

// 数据读取完毕, 循环正常退出!
System.out.println( "[MessageFileManager] 恢复 Message 数据完成!");
}
return messages;
}30
31
32
33
34
•使⽤DataInputStream 读取数据.先读4个字节为消息的⻓度,然后再按照这个⻓度来读取实际消息内容.
•读取完毕之后,转换成Message 对象.
•同时计算出该对象的offsetBeg 和offsetEnd.
•最终把结果整理成链表,返回出去.
•注意,对于DataInputStream 来说,如果读取到EOF, 会抛出⼀个EOFException ,⽽不是返回特定值.因此需要注意上述循环的结束条件.
实现垃圾回收(GC)
上述删除操作,只是把消息在⽂件上标记成了⽆效.并没有腾出硬盘空间.最终⽂件⼤⼩可能会越积越多.因此需要定期的进⾏批量清除.
此处使⽤类似于复制算法.当总消息数超过2000, 并且有效消息数⽬少于50%的时候,就触发GC.
GC的时候会把所有有效消息加载出来,写⼊到⼀个新的消息⽂件中,使⽤新⽂件,代替旧⽂件即可.
// 检查是否要针对⽂件进⾏ GC 操作
public boolean checkGC(String queueName) {
Stat stat = readStat(queueName);
if (stat.totalCount >= 2000 && (double)stat.validCount / ( double)
stat.totalCount <= 0.5) {
return true;
}
return false;
}
private String getQueueDataNewPath (String queueName) {
return getQueueDir(queueName) + "/queue_data_new.txt" ;
}
// 真正执⾏ GC 操作
// 使⽤复制算法.
// 先创建⼀个新的⽂件, 名字为 "queue_data_new.txt"
// 然后加载出旧的⽂件的所有有效消息内容
// 把这些内容写⼊到新的⽂件中. 1
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

// 删除旧⽂件, 对新⽂件重命名.
public void gc(MSGQueue queue) throws MqException, IOException,
ClassNotFoundException {
synchronized (queue) {
long gcBeg = System.currentTimeMillis();
// 1. 创建⼀个新的⽂件, 名字为 "queue_data_new.txt"
File queueDataNew = new File(getQueueDataNewPath(queue.getName()));
if (queueDataNew.exists()) {
throw new MqException ("[MessageFileManager] gc 时发现队列新数据⽂件已经存在! queueName=" + queue.getName());
}
boolean ok = queueDataNew.createNewFile();
if (!ok) {
throw new IOException ("创建⽂件失败! queueDataNew=" +
queueDataNew.getAbsolutePath());
}
// 2. 遍历旧⽂件, 读取出每个对象 (只保留有效消息)
List<Message> messageList = loadAllMessageFromQueue(queue.getName());
// 3. 把有效消息写⼊到新的⽂件中.
try (OutputStream outputStream = new FileOutputStream (queueDataNew)) {
DataOutputStream dataOutputStream = new
DataOutputStream (outputStream);
for (Message message : messageList) {
byte[] buffer = BinaryTool.toBytes(message);
dataOutputStream.writeInt(buffer.length);
dataOutputStream.write(buffer);
}
}
// 4. 删除 queue_data.txt, 把 queue_data_new.txt 重命名为 queue_data
File queueDataOld = new File(getQueueDataPath(queue.getName()));
ok = queueDataOld.delete();
if (!ok) {
throw new IOException ("删除⽂件失败! queueDataOld=" +
queueDataOld.getAbsolutePath());
}
ok = queueDataNew.renameTo(queueDataOld);
if (!ok) {
throw new IOException ("⽂件重命名失败! queueDataOld=" +
queueDataOld.getAbsolutePath() +
", queueDataNew=" + queueDataNew.getAbsolutePath());
}
// 5. 更新统计⽂件
Stat stat = readStat(queue.getName());
stat.validCount = messageList.size();
stat.totalCount = messageList.size();
writeStat(queue.getName(), stat);19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59

long gcEnd = System.currentTimeMillis();
System.out.println( "[MessageFileManager] gc 执⾏完毕! queueName=" +
queue.getName() + ", time=" + (gcEnd - gcBeg) + "ms");
}
}60
61
62
63
如果⽂件很⼤,消息⾮常多,可能⽐较低效,这种就需要把⽂件做拆分和合并了.
Rabbitmq 本体是这样实现的.但是咱们此处为了实现简单,就不做这个了.
测试MessageFileManager
创建MessageFileManagerTests 编写测试⽤例代码.
•创建两个队列,⽤来辅助测试.
•使⽤ReflectionTestUtils.invokeMethod 来调⽤私有⽅法.
@SpringBootTest
public class MessageFileManagerTests {
private String queueName1 = "testQueue1" ;
private String queueName2 = "testQueue2" ;
private MessageFileManager messageFileManager = new MessageFileManager ();
@BeforeEach
public void setUp() throws IOException {
messageFileManager.createQueueFiles(queueName1);
messageFileManager.createQueueFiles(queueName2);
}
@AfterEach
public void tearDown () throws IOException {
messageFileManager.destroyQueueFiles(queueName1);
messageFileManager.destroyQueueFiles(queueName2);
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
@Test
public void testCreateFile () {
File queueDataFile1 = new File("./data/" + queueName1 + "/queue_data.txt" );
Assertions.assertEquals( true, queueDataFile1.isFile());
File queueStatFile1 = new File("./data/" + queueName1 + "/queue_stat.txt" );1
2
3
4
5

Assertions.assertEquals( true, queueStatFile1.isFile());
Assertions.assertTrue(queueStatFile1.length() > 0);
File queueDataFile2 = new File("./data/" + queueName2 + "/queue_data.txt" );
Assertions.assertEquals( true, queueDataFile2.isFile());
File queueStatFile2 = new File("./data/" + queueName2 + "/queue_stat.txt" );
Assertions.assertEquals( true, queueStatFile2.isFile());
Assertions.assertTrue(queueStatFile2.length() > 0);
}
@Test
public void testReadWriteStat () {
MessageFileManager. Stat stat = new MessageFileManager .Stat();
stat.totalCount = 100;
stat.validCount = 50;
// 通过 Spring 提供的反射⼯具类, 调⽤私有⽅法.
ReflectionTestUtils.invokeMethod(messageFileManager, "writeStat" ,
queueName1, stat);
MessageFileManager. Stat newStat =
ReflectionTestUtils.invokeMethod(messageFileManager, "readStat" , queueName1);
Assertions.assertEquals( 100, newStat.totalCount);
Assertions.assertEquals( 50, newStat.validCount);
}
private MSGQueue createTestQueue (String queueName) {
MSGQueue queue = new MSGQueue ();
queue.setName(queueName);
queue.setDurable( true);
queue.setAutoDelete( true);
queue.setExclusive( true);
HashMap<String, Object> hashMap = new HashMap<>();
hashMap.put( "aaa", "111");
hashMap.put( "bbb", "222");
queue.setArguments(hashMap);
return queue;
}
private Message createTestMessage (String content) {
Message message = new Message();
message.setMessageId( "M-" + UUID.randomUUID().toString());
message.setRoutingKey( "testRoutingKey" );
message.setDeliveryMode( 2);
message.setBody(content.getBytes());
return message;
}
@Test6
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
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49

public void testSendMessage () throws IOException, MqException,
ClassNotFoundException {
Message message = createTestMessage( "testMessage" );
MSGQueue queue = createTestQueue(queueName1);
messageFileManager.sendMessage(queue, message);
// 检查 stat ⽂件
MessageFileManager. Stat newStat =
ReflectionTestUtils.invokeMethod(messageFileManager, "readStat" , queueName1);
Assertions.assertEquals( 1, newStat.totalCount);
Assertions.assertEquals( 1, newStat.validCount);
// 读⽂件内容
List<Message> messageList =
messageFileManager.loadAllMessageFromQueue(queueName1);
Assertions.assertEquals( 1, messageList.size());
Message curMessage = messageList.get( 0);
Assertions.assertEquals(message.getMessageId(), curMessage.getMessageId());
Assertions.assertEquals(message.getRoutingKey(),
curMessage.getRoutingKey());
Assertions.assertEquals(message.getDeliveryMode(),
curMessage.getDeliveryMode());
Assertions.assertArrayEquals(message.getBody(), curMessage.getBody());
}
@Test
public void testLoadAllMessageFromQueue () throws IOException, MqException,
ClassNotFoundException {
MSGQueue queue = createTestQueue(queueName1);
List<Message> expectedMessages = new ArrayList <>();
for (int i = 0; i < 100; i++) {
Message message = createTestMessage( "testMessage" );
messageFileManager.sendMessage(queue, message);
expectedMessages.add(message);
}
List<Message> actualMessages =
messageFileManager.loadAllMessageFromQueue(queueName1);
Assertions.assertEquals( 100, actualMessages.size());
for (int i = 0; i < 100; i++) {
Message expectedMessage = actualMessages.get(i);
Message actualMessage = actualMessages.get(i);
System.out.println( "[" + i + "] " + actualMessage);
Assertions.assertEquals(expectedMessage.getMessageId(),
actualMessage.getMessageId());
Assertions.assertEquals(expectedMessage.getRoutingKey(),
actualMessage.getRoutingKey());50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86

Assertions.assertEquals(expectedMessage.getDeliveryMode(),
actualMessage.getDeliveryMode());
Assertions.assertArrayEquals(expectedMessage.getBody(),
actualMessage.getBody());
Assertions.assertEquals( 0x1, actualMessage.getIsValid());
}
}
@Test
public void testDeleteMessage () throws IOException, MqException,
ClassNotFoundException {
MSGQueue queue = createTestQueue(queueName1);
List<Message> expectedMessages = new ArrayList <>();
for (int i = 0; i < 10; i++) {
Message message = createTestMessage( "testMessage" );
messageFileManager.sendMessage(queue, message);
expectedMessages.add(message);
}
System.out.println( "expected:" + expectedMessages);
messageFileManager.deleteMessage(queue, expectedMessages.get( 0));
messageFileManager.deleteMessage(queue, expectedMessages.get( 1));
messageFileManager.deleteMessage(queue, expectedMessages.get( 2));
// 读出来, 这个⽅法只能加载有效数据.
List<Message> actualMessages =
messageFileManager.loadAllMessageFromQueue(queueName1);
System.out.println( "actual: " + actualMessages);
Assertions.assertEquals( 7, actualMessages.size());
for (int i = 0; i < actualMessages.size(); i++) {
Assertions.assertEquals(expectedMessages.get(i + 3).getMessageId(),
actualMessages.get(i).getMessageId());
}
}
@Test
public void testGc() throws IOException, MqException, ClassNotFoundException {
MSGQueue queue = createTestQueue(queueName1);
List<Message> expectedMessages = new ArrayList <>();
// 创建 100 个元素
for (int i = 0; i < 100; i++) {
Message message = createTestMessage( "testMessage" );
messageFileManager.sendMessage(queue, message);
expectedMessages.add(message);
}
// 删除偶数下标的元素
for (int i = 0; i < 100; i += 2) {87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128

messageFileManager.deleteMessage(queue, expectedMessages.get(i));
}
// 获取旧⽂件⼤⼩
File oldFile = new File("./data/" + queueName1 + "/queue_data.txt" );
long oldLength = oldFile.length();
// 调⽤ gc
messageFileManager.gc(queue);
// 重新读⽂件
List<Message> actualMessages =
messageFileManager.loadAllMessageFromQueue(queueName1);
Assertions.assertEquals( 50, actualMessages.size());
for (int i = 0; i < 50; i++) {
// 注意这⾥的下标换算
Assertions.assertEquals(expectedMessages.get( 2 * i +
1).getMessageId(), actualMessages.get(i).getMessageId());
}
// 获取新⽂件⼤⼩
File newFile = new File("./data/" + queueName1 + "/queue_data.txt" );
long newLength = newFile.length();
System.out.println( "oldLength=" + oldLength);
System.out.println( "newLength=" + newLength);
Assertions.assertTrue(oldLength > newLength);
}129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
⼋.整合数据库和⽂件上述代码中,使⽤数据库存储了Exchange, Queue, Binding, 使⽤⽂本⽂件存储了Message.
接下来我们把两个部分整合起来,统⼀进⾏管理.
创建DiskDataCenter
使⽤DiskDataCenter 来综合管理数据库和⽂本⽂件的内容.
DiskDataCenter 会持有DataBaseManager 和MessageFileManager 对象.
// 管理硬盘上的数据.
// 分成两个部分:
// 1. 数据库管理元信息
// 2. ⽂件管理消息内容
public class DiskDataCenter {
private String virtualHostName;1
2
3
4
5
6

// 管理数据库中的元数据
private DataBaseManager dataBaseManager = new DataBaseManager ();
// 管理⽂件中的消息数据
private MessageFileManager messageFileManager = new MessageFileManager ();
public void init(String virtualHostName) {
this.virtualHostName = virtualHostName;
initDir();
dataBaseManager.init();
messageFileManager.init();
}
}7
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
实现initDir
// 初始化⽬录结构
// virtualHostName 为 default-VirtualHost
// 则存放数据的⽬录名为: ./data/default-VirtualHost/
private void initDir() {
File baseDir = new File("./data/" + virtualHostName);
if (!baseDir.exists()) {
boolean ok = baseDir.mkdirs();
if (ok) {
System.out.println( "[DiskDataCenter] 初始化数据⽬录完成!");
} else {
System.out.println( "[DiskDataCenter] 初始化数据⽬录失败!");
}
} else {
System.out.println( "[DiskDataCenter] 数据⽬录已经存在!");
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
封装Exchange ⽅法
public void insertExchange (Exchange exchange) {
dataBaseManager.insertExchange(exchange);
}
public void deleteExchange (String exchangeName) {1
2
3
4
5

dataBaseManager.deleteExchange(exchangeName);
}
public List<Exchange> selectAllExchanges () {
return dataBaseManager.selectAllExchanges();
}6
7
8
9
10
11
封装Queue ⽅法
public void insertQueue (MSGQueue queue) throws IOException {
dataBaseManager.insertQueue(queue);
messageFileManager.createQueueFiles(queue.getName());
}
public void deleteQueue (String queueName) throws IOException {
dataBaseManager.deleteQueue(queueName);
messageFileManager.destroyQueueFiles(queueName);
}
public List<MSGQueue> selectAllQueues () {
return dataBaseManager.selectAllQueues();
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
•创建/删除队列的时候同时创建/删除队列⽬录.
封装Binding ⽅法
public void insertBinding (Binding binding) {
dataBaseManager.insertBinding(binding);
}
public void deleteBinding (Binding binding) {
dataBaseManager.deleteBinding(binding);
}
public List<Binding> selectAllBindings () {
return dataBaseManager.selectAllBindings();
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

封装Message ⽅法
public void sendMessage (MSGQueue queue, Message message) throws MqException,
IOException {
messageFileManager.sendMessage(queue, message);
}
public void deleteMessage (MSGQueue queue, Message message) throws MqException,
IOException, ClassNotFoundException {
messageFileManager.deleteMessage(queue, message);
// 判定是否要 GC
if (messageFileManager.checkGC(queue.getName())) {
messageFileManager.gc(queue);
}
}
public LinkedList<Message> loadAllMessageFromQueue (String queueName) throws
MqException, IOException, ClassNotFoundException {
return messageFileManager.loadAllMessageFromQueue(queueName);
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
•在deleteMessage 的时候判定是否进⾏GC.
⼩结通过上述封装,把数据库和硬盘⽂件两部分合并成⼀个整体.上层代码在调⽤的时候则不再关⼼该数据是存储在哪个部分的.
这个类的整体实现并不复杂,关键逻辑在之前都已经准备好了.
该类我们就不单独进⾏单元测试了.同学们可以⾃⾏完成.
九.内存数据结构设计硬盘上存储数据,只是为了实现"持久化"这样的效果.但是实际的消息存储/转发,还是主要靠内存的结构.
对于MQ来说,内存部分是更关键的,内存速度更快,可以达成更⾼的并发.

创建MemoryDataCenter
创建mqserver.datacenter.MemoryDataCenter
// 管理所有的内存数据.
public class MemoryDataCenter {
// key 是 exchangeName
private ConcurrentHashMap<String, Exchange> exchangeMap = new
ConcurrentHashMap <>();
// key 是 queueName
private ConcurrentHashMap<String, MSGQueue> queueMap = new
ConcurrentHashMap <>();
// 第⼀个 key 是 exchangeName, 第⼆个 key 是 queueName
private ConcurrentHashMap<String, HashMap<String, Binding>> bindingsMap =
new ConcurrentHashMap <>();
// 保存所有消息, key 是 messageId
private ConcurrentHashMap<String, Message> messageMap = new
ConcurrentHashMap <>();
// key 是 queueName
private ConcurrentHashMap<String, LinkedList<Message>> queueMessageMap =
new ConcurrentHashMap <>();
// ⽤来存放待确认的消息
// key1 是 queueName, key2 是 messageId.
// 这个结构不需要有对应的硬盘数据. 换句话说, 如果某个消息消费了, 但是没有 ack, 这个时候 broker 宕机了, 那么重启 broker 之后
// 就把刚才的消息当做从来没消费过.
private ConcurrentHashMap<String, HashMap<String, Message>>
queueMessageWaitAck = new ConcurrentHashMap <>();
public void init() {
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
21
•使⽤四个哈希表,管理Exchange, Queue, Binding, Message.
•使⽤⼀个哈希表+链表管理队列->消息之间的关系.
•使⽤⼀个哈希表+哈希表管理所有的未被确认的消息.
为了保证消息被正确消费了,会使⽤两种⽅式进⾏确认.⾃动ACK和⼿动ACK.
其中⾃动ACK是指当消息被消费之后,就会⽴即被销毁释放.
其中⼿动ACK是指当消息被消费之后,由消费者主动调⽤⼀个basicAck ⽅法,进⾏主动确认.服务器收到这个确认之后,才能真正销毁消息.
此处的"未确认消息"就是指在⼿动ACK模式下,该消息还没有被调⽤basicAck. 此时消息不能删除,
但是要和其他未消费的消息区分开.于是另搞了个结构.

当后续basicAck 到了,就可以删除消息了.
封装Exchange ⽅法
public void insertExchange (Exchange exchange) {
exchangeMap.put(exchange.getName(), exchange);
}
public Exchange getExchange (String exchangeName) {
return exchangeMap.get(exchangeName);
}
public void deleteExchange (String exchangeName) {
exchangeMap.remove(exchangeName);
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
封装Queue ⽅法
public void insertQueue (MSGQueue queue) {
queueMap.put(queue.getName(), queue);
}
public MSGQueue getQueue (String queueName) {
return queueMap.get(queueName);
}
public void deleteQueue (String queueName) {
queueMap.remove(queueName);
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
封装Binding ⽅法
public void insertBinding (Binding binding) throws MqException {
HashMap<String, Binding> bindingMap =
bindingsMap.computeIfAbsent(binding.getExchangeName(), k -> new HashMap<>());
synchronized (bindingMap) {1
2
3

// 不存在就创建⼀份
if (bindingMap.get(binding.getQueueName()) != null) {
throw new MqException ("[MemoryDataCenter] 绑定已经存在!
exchangeName=" + binding.getExchangeName()
+ ", queueName=" + binding.getQueueName());
}
bindingMap.put(binding.getQueueName(), binding);
}
}
public Binding getBinding (String queueName, String exchangeName) {
HashMap<String, Binding> bindingMap = bindingsMap.get(exchangeName);
if (bindingMap == null) {
return null;
}
synchronized (bindingMap) {
return bindingMap.get(queueName);
}
}
public void deleteBinding (Binding binding) throws MqException {
HashMap<String, Binding> bindingMap =
bindingsMap.get(binding.getExchangeName());
if (bindingMap == null) {
throw new MqException ("[MemoryDataCenter] 绑定不存在! exchangeName=" +
binding.getExchangeName()
+ ", queueName=" + binding.getQueueName());
}
synchronized (bindingMap) {
Binding toDelete = bindingMap.get(binding.getQueueName());
if (toDelete == null) {
throw new MqException ("[MemoryDataCenter] 绑定不存在! exchangeName="
+ binding.getExchangeName()
+ ", queueName=" + binding.getQueueName());
}
bindingMap.remove(binding.getQueueName());
}
}
public Map<String, Binding> getBindingsByExchange (String exchangeName) {
return bindingsMap.get(exchangeName);
}4
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
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
封装Message ⽅法

// 查询指定的消息
public Message getMessage (String messageId) {
return messageMap.get(messageId);
}
// 向消息中⼼中添加消息
public void addMessage (Message message) {
messageMap.put(message.getMessageId(), message);
System.out.println( "[MemoryCenter] 新消息被添加! messageId=" +
message.getMessageId());
}
// 从消息中⼼删除消息
public void removeMessage (String messageId) {
messageMap.remove(messageId);
System.out.println( "[MemoryCenter] 消息被彻底删除! messageId=" + messageId);
}
// 发送消息到指定队列中
public void sendMessage (MSGQueue queue, Message message) {
List<Message> messageList =
queueMessageMap.computeIfAbsent(queue.getName(), k -> new LinkedList <>());
synchronized (messageList) {
messageList.add(message);
}
// 如果消息已经存在, 重复调⽤也没啥⼤不了的.
addMessage(message);
System.out.println( "[MemoryCenter] 消息被投递到队列中! messageId=" +
message.getMessageId() + ", queueName=" + queue.getName());
}
// 从指定队列中取消息.
public Message pollMessage (String queueName) throws MqException {
List<Message> messageList = queueMessageMap.get(queueName);
if (messageList == null) {
throw new MqException ("[MemoryDataCenter] 队列不存在! queueName=" +
queueName);
}
synchronized (messageList) {
if (messageList.size() == 0) {
return null;
}
// 出队列头元素
Message currentMessage = messageList.remove( 0);
System.out.println( "[MemoryCenter] 消息从队列中取出! messageId=" +
currentMessage.getMessageId() + ", queueName=" + queueName);1
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
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41

return currentMessage;
}
}
public int getMessageCount (String queueName) throws MqException {
List<Message> messageList = queueMessageMap.get(queueName);
if (messageList == null) {
// 如果队列不存在, 则直接返回⻓度 0, 说明该 queueName 下还没有消息.
return 0;
}
synchronized (messageList) {
return messageList.size();
}
}42
43
44
45
46
47
48
49
50
51
52
53
54
55
针对未确认的消息的处理
// 未被确认的消息, 先临时存放⼀下
public void addMessageWaitAck (String queueName, Message message) {
HashMap<String, Message> messageHashMap =
queueMessageWaitAck.computeIfAbsent(queueName, k -> new HashMap<>());
synchronized (messageHashMap) {
messageHashMap.put(message.getMessageId(), message);
}
System.out.println( "[MemoryCenter] 消息进⼊待确认队列! messageId=" +
message.getMessageId() + ", queueName=" + queueName);
}
// 消息被确认之后, 就可以真正删除了.
public void removeMessageWaitAck (String queueName, String messageId) {
HashMap<String, Message> messageHashMap =
queueMessageWaitAck.get(queueName);
if (messageHashMap == null) {
return;
}
synchronized (messageHashMap) {
messageHashMap.remove(messageId);
}
System.out.println( "[MemoryCenter] 消息从待确认队列删除! messageId=" +
messageId + ", queueName=" + queueName);
}
public Message getMessageWaitAck (String queueName, String messageId) {1
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
21
22

HashMap<String, Message> messageHashMap =
queueMessageWaitAck.get(queueName);
if (messageHashMap == null) {
return null;
}
synchronized (messageHashMap) {
return messageHashMap.get(messageId);
}
}23
24
25
26
27
28
29
30
实现重启后恢复内存
// 从硬盘上恢复数据
public void recovery (DiskDataCenter diskDataCenter) throws MqException,
IOException, ClassNotFoundException {
// 1. 恢复交换机数据
List<Exchange> exchanges = diskDataCenter.selectAllExchanges();
for (Exchange exchange : exchanges) {
exchangeMap.put(exchange.getName(), exchange);
}
// 2. 恢复队列数据
List<MSGQueue> queues = diskDataCenter.selectAllQueues();
for (MSGQueue queue : queues) {
queueMap.put(queue.getName(), queue);
}
// 3. 恢复绑定数据
List<Binding> bindings = diskDataCenter.selectAllBindings();
for (Binding binding : bindings) {
HashMap<String, Binding> bindingMap =
bindingsMap.computeIfAbsent(binding.getExchangeName(), k -> new HashMap<>());
bindingMap.put(binding.getQueueName(), binding);
}
// 4. 恢复消息数据
// 只需要恢复 queueMessageMap 和 messageMap
// queueMessageWaitAck 则不必恢复. 未被确认的消息只是在内存存储. 如果这个时候
broker 宕机了, 则消息视为没有被消费过.
for (MSGQueue queue : queues) {
LinkedList<Message> messages =
diskDataCenter.loadAllMessageFromQueue(queue.getName());
queueMessageMap.put(queue.getName(), messages);
for (Message message : messages) {
messageMap.put(message.getMessageId(), message);
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
21
22
23
24
25
26
27

}
}28
29
测试MemoryDataCenter
创建MemoryDataCenterTests
@SpringBootTest
public class MemoryDataCenterTests {
private MemoryDataCenter memoryDataCenter = null;
@BeforeEach
public void setUp() {
memoryDataCenter = new MemoryDataCenter ();
memoryDataCenter.init();
}
@AfterEach
public void tearDown () {
memoryDataCenter = null;
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
private Exchange createTestExchange (String exchangeName) {
Exchange exchange = new Exchange ();
exchange.setName(exchangeName);
exchange.setType(ExchangeType.FANOUT);
exchange.setAutoDelete( true);
exchange.setDurable( true);
HashMap<String, Object> arguments = new HashMap<>();
arguments.put( "aaa", "111");
arguments.put( "bbb", "222");
exchange.setArguments(arguments);
return exchange;
}
private MSGQueue createTestQueue (String queueName) {
MSGQueue queue = new MSGQueue ();
queue.setName(queueName);
queue.setDurable( true);
queue.setAutoDelete( true);
queue.setExclusive( true);1
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

HashMap<String, Object> hashMap = new HashMap<>();
hashMap.put( "aaa", "111");
hashMap.put( "bbb", "222");
queue.setArguments(hashMap);
return queue;
}
@Test
public void testExchange () {
Exchange expectedExchange = createTestExchange( "testExchange" );
memoryDataCenter.insertExchange(expectedExchange);
Exchange actualExchange = memoryDataCenter.getExchange( "testExchange" );
Assertions.assertEquals(expectedExchange, actualExchange);
memoryDataCenter.deleteExchange( "testExchange" );
actualExchange = memoryDataCenter.getExchange( "testExchange" );
Assertions.assertNull(actualExchange);
}
@Test
public void testQueue () {
MSGQueue expectedQueue = createTestQueue( "testQueue" );
memoryDataCenter.insertQueue(expectedQueue);
MSGQueue actualQueue = memoryDataCenter.getQueue( "testQueue" );
Assertions.assertEquals(expectedQueue, actualQueue);
memoryDataCenter.deleteQueue( "testQueue" );
actualQueue = memoryDataCenter.getQueue( "testQueue" );
Assertions.assertNull(actualQueue);
}
@Test
public void testBinding () throws MqException {
Binding expectedBinding = new Binding();
expectedBinding.setQueueName( "testQueue" );
expectedBinding.setExchangeName( "testExchange" );
expectedBinding.setBindingKey( "testBindingKey" );
memoryDataCenter.insertBinding(expectedBinding);
Binding actualBinding = memoryDataCenter.getBinding( "testQueue" ,
"testExchange" );
Assertions.assertEquals(expectedBinding, actualBinding);
Map<String, Binding> bindingMap =
memoryDataCenter.getBindingsByExchange( "testExchange" );20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64

actualBinding = bindingMap.get( "testQueue" );
Assertions.assertEquals(expectedBinding, actualBinding);
memoryDataCenter.deleteBinding(expectedBinding);
actualBinding = memoryDataCenter.getBinding( "testQueue" , "testExchange" );
Assertions.assertNull(actualBinding);
}
private Message createTestMessage (String content) {
Message message = new Message();
message.setMessageId( "M-" + UUID.randomUUID().toString());
message.setRoutingKey( "testRoutingKey" );
message.setDeliveryMode( 2);
message.setBody(content.getBytes());
return message;
}
@Test
public void testMessage () {
Message expectedMessage = createTestMessage( "testMessage" );
memoryDataCenter.addMessage(expectedMessage);
Message actualMessage =
memoryDataCenter.getMessage(expectedMessage.getMessageId());
Assertions.assertEquals(expectedMessage, actualMessage);
memoryDataCenter.removeMessage(expectedMessage.getMessageId());
actualMessage =
memoryDataCenter.getMessage(expectedMessage.getMessageId());
Assertions.assertNull(actualMessage);
}
@Test
public void testSendMessage () throws MqException {
MSGQueue queue = createTestQueue( "testQueue" );
List<Message> expectedMessages = new ArrayList <>();
for (int i = 0; i < 10; i++) {
Message message = createTestMessage( "testMessage" );
memoryDataCenter.sendMessage(queue, message);
expectedMessages.add(message);
}
List<Message> actualMessages = new ArrayList <>();
while (true) {
Message message = memoryDataCenter.pollMessage( "testQueue" );
if (message == null) {
break;65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109

}
actualMessages.add(message);
}
Assertions.assertEquals(expectedMessages.size(), actualMessages.size());
for (int i = 0; i < expectedMessages.size(); i++) {
Assertions.assertEquals(expectedMessages.get(i),
actualMessages.get(i));
}
}
@Test
public void testMessageWaitAck () {
Message expectedMessage = createTestMessage( "testMessage" );
memoryDataCenter.addMessageWaitAck( "testQueue" , expectedMessage);
Message actualMessage = memoryDataCenter.getMessageWaitAck( "testQueue" ,
expectedMessage.getMessageId());
Assertions.assertEquals(expectedMessage, actualMessage);
memoryDataCenter.removeMessageWaitAck( "testQueue" ,
expectedMessage.getMessageId());
actualMessage = memoryDataCenter.getMessageWaitAck( "testQueue" ,
expectedMessage.getMessageId());
Assertions.assertNull(actualMessage);
}
@Test
public void testRecovery () throws IOException, MqException,
ClassNotFoundException {
JavaMessageQueueApplication.ac =
SpringApplication.run(JavaMessageQueueApplication.class);
// 构造初始数据
DiskDataCenter diskDataCenter = new DiskDataCenter ();
diskDataCenter.init( "");
Exchange expectedExchange = createTestExchange( "testExchange" );
diskDataCenter.insertExchange(expectedExchange);
MSGQueue expectedQueue = createTestQueue( "testQueue" );
diskDataCenter.insertQueue(expectedQueue);
Binding expectedBinding = new Binding();
expectedBinding.setExchangeName( "testExchange" );
expectedBinding.setQueueName( "testQueue" );
expectedBinding.setBindingKey( "testBindingKey" );
diskDataCenter.insertBinding(expectedBinding);110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150

Message expectedMessage = createTestMessage( "testMessage" );
diskDataCenter.sendMessage(expectedQueue, expectedMessage);
// 恢复数据
memoryDataCenter.recovery(diskDataCenter);
// 对⽐结果
Exchange actualExchange = memoryDataCenter.getExchange( "testExchange" );
Assertions.assertEquals(expectedExchange.getType(),
actualExchange.getType());
Assertions.assertEquals(expectedExchange.isDurable(),
actualExchange.isDurable());
Assertions.assertEquals(expectedExchange.isAutoDelete(),
actualExchange.isAutoDelete());
Assertions.assertEquals(expectedExchange.getArguments(),
actualExchange.getArguments());
MSGQueue actualQueue = memoryDataCenter.getQueue( "testQueue" );
Assertions.assertEquals(expectedQueue.isDurable(),
actualQueue.isDurable());
Assertions.assertEquals(expectedQueue.isAutoDelete(),
actualQueue.isAutoDelete());
Assertions.assertEquals(expectedQueue.isExclusive(),
actualQueue.isExclusive());
Assertions.assertEquals(expectedQueue.getArguments(),
actualQueue.getArguments());
Binding actualBinding = memoryDataCenter.getBinding( "testQueue" ,
"testExchange" );
Assertions.assertEquals(expectedBinding.getBindingKey(),
actualBinding.getBindingKey());
// 清理
JavaMessageQueueApplication.ac.close();
File dbFile = new File("meta.db" );
dbFile.delete();
File dataFile = new File("./data" );
FileUtils.deleteDirectory(dataFile);
}151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
⼗.虚拟主机设计

⾄此,内存和硬盘的数据都已经组织完成.接下来使⽤"虚拟主机"这个概念,把这两部分的数据也串起来.
并且实现⼀些MQ的关键API.
注意:在RabbitMQ 中,虚拟主机是可以随意创建/删除的.咱们此处为了实现简单,并没有实现虚拟主机的管理.因此我们默认就只有⼀个虚拟主机的存在.但是在数据结构的设计上我们预留了对于多虚拟主机的管理.
保证不同虚拟主机中的Exchange, Queue, Binding, Message 都是相互隔离的.
创建VirtualHost
创建mqserver.VirtualHost
public class VirtualHost {
private String virtualhostName;
private DiskDataCenter diskDataCenter = new DiskDataCenter ();
private MemoryDataCenter memoryDataCenter = new MemoryDataCenter ();
private Router router = new Router();
private ConsumerManager consumerManager = new ConsumerManager (this);
}1
2
3
4
5
6
7
其中Router ⽤来定义转发规则,ConsumerManager ⽤来实现消息消费.这两个内容后续再介绍实现构造⽅法和getter
构造⽅法中会针对DiskDataCenter 和MemoryDataCenter 进⾏初始化.
同时会把硬盘的数据恢复到内存中.
public VirtualHost (String virtualhostName) {
this.virtualhostName = virtualhostName;
// 先初始化硬盘数据
diskDataCenter.init(virtualhostName);
// 后初始化内存数据
memoryDataCenter.init();
try {
// 进⾏恢复操作
memoryDataCenter.recovery(diskDataCenter);1
2
3
4
5
6
7
8
9
10

} catch (Exception e) {
e.printStackTrace();
System.out.println( "[VirtualHost] 恢复内存数据失败!");
}
}
public String getVirtualhostName () {
return virtualhostName;
}
public DiskDataCenter getDiskDataCenter () {
return diskDataCenter;
}
public MemoryDataCenter getMemoryDataCenter () {
return memoryDataCenter;
}11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
创建交换机
•此处的autoDelete, arguments 其实并没有使⽤.只是先预留出来.(RabbitMQ 是⽀持的).
•约定,交换机/队列的名字,都加上VirtualHostName 作为前缀.这样不同VirtualHost 中就可以存在同名的交换机或者队列了.
•exchangeDeclare 的语义是,不存在就创建,存在则直接返回.因此不叫做"exchangeCreate".
•先写硬盘,后写内存.因为写硬盘失败概率更⼤.如果硬盘写失败了,也就不必写内存了.
// 创建交换机
// 先写硬盘, 后写内存. 写硬盘失败概率更⼤, 如果异常了, 也就不写内存了.
public boolean exchangeDeclare (String exchangeName, ExchangeType exchangeType,
boolean durable, boolean autoDelete,
Map<String, Object> arguments) {
// 真实的 exchangeName 需要拼接上 virtualhostName
exchangeName = virtualhostName + exchangeName;
try {
// 1. 判定该交换机是否存在
Exchange existsExchange = memoryDataCenter.getExchange(exchangeName);
if (existsExchange != null) {
System.out.println( "[VirtualHost] 交换机已经存在! exchangeName=" +
exchangeName);
return true;
}
// 2. 构造 Exchange 对象 1
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

Exchange exchange = new Exchange ();
exchange.setName(exchangeName);
exchange.setType(exchangeType);
exchange.setDurable(durable);
exchange.setAutoDelete(autoDelete);
exchange.setArguments(arguments);
// 3. 把数据写⼊硬盘
if (durable) {
diskDataCenter.insertExchange(exchange);
}
// 4. 把数据写⼊内存
memoryDataCenter.insertExchange(exchange);
System.out.println( "[VirtualHost] 交换机创建完成! exchangeName=" +
exchangeName);
return true;
} catch (Exception e) {
System.out.println( "[VirtualHost] 交换机创建失败! exchangeName=" +
exchangeName);
e.printStackTrace();
return false;
}
}15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
删除交换机
// 删除交换机
// 先写硬盘, 后写内存. 写硬盘失败概率更⼤, 如果异常了, 也就不写内存了.
public boolean exchangeDelete (String exchangeName) {
// 真实的 exchangeName 需要拼接上 virtualhostName
exchangeName = virtualhostName + exchangeName;
try {
// 1. 先找到对应的交换机.
Exchange toDelete = memoryDataCenter.getExchange(exchangeName);
if (toDelete == null) {
throw new MqException ("[VirtualHost] 交换机不存在, ⽆法删除!");
}
// 2. 删除硬盘上的交换机数据
if (toDelete.isDurable()) {
diskDataCenter.deleteExchange(exchangeName);
}
// 3. 删除内存中的交换机数据
memoryDataCenter.deleteExchange(exchangeName);1
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

System.out.println( "[VirtualHost] 交换机删除成功! exchangeName=" +
exchangeName);
return true;
} catch (Exception e) {
System.out.println( "[VirtualHost] 交换机删除失败! exchangeName=" +
exchangeName);
e.printStackTrace();
return false;
}
}18
19
20
21
22
23
24
25
创建队列
// 创建队列
public boolean queueDeclare (String queueName, boolean durable, boolean
exclusive, boolean autoDelete,
Map<String, Object> arguments) {
// 真实的 queueName 需要拼接上 virtualhostName
queueName = virtualhostName + queueName;
try {
// 1. 判定队列是否存在
MSGQueue existsQueue = memoryDataCenter.getQueue(queueName);
if (existsQueue != null) {
System.out.println( "[VirtualHost] 队列已经存在! queueName=" +
queueName);
return true;
}
// 2. 创建队列对象
MSGQueue queue = new MSGQueue ();
queue.setName(queueName);
queue.setDurable(durable);
queue.setAutoDelete(autoDelete);
queue.setArguments(arguments);
// 3. 写硬盘
if (durable) {
diskDataCenter.insertQueue(queue);
}
// 4. 写内存
memoryDataCenter.insertQueue(queue);
System.out.println( "[VirtualHost] 队列创建成功! queueName=" + queueName);
return true;
} catch (Exception e) {
System.out.println( "[VirtualHost] 队列创建失败! queueName=" + queueName);1
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
21
22
23
24
25
26
27
28

e.printStackTrace();
return false;
}
}29
30
31
32
删除队列
// 删除队列
public boolean queueDelete (String queueName) {
// 真实的 queueName 需要拼接上 virtualhostName
queueName = virtualhostName + queueName;
try {
// 1. 根据 queueName 查询对应的队列对象
MSGQueue queue = memoryDataCenter.getQueue(queueName);
if (queue == null) {
throw new MqException ("[VirtualHost] 队列不存在, ⽆法删除!");
}
// 2. 删除硬盘数据
if (queue.isDurable()) {
diskDataCenter.deleteQueue(queueName);
}
// 3. 删除内存数据
memoryDataCenter.deleteQueue(queueName);
System.out.println( "[VirtualHost] 队列删除成功! queueName=" + queueName);
return true;
} catch (Exception e) {
System.out.println( "[VirtualHost] 队列删除失败! queueName=" + queueName);
e.printStackTrace();
return false;
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
21
22
23
24
创建绑定
•bindingKey 是进⾏topic 转发时的⼀个关键概念.使⽤router 类来检测是否是合法的bindingKey.
•后续再介绍router.checkBindingKeyValid 的实现.此处先留空.
// 创建绑定 1

public boolean queueBind (String queueName, String exchangeName, String
bindingKey) {
// 真实的 queueName 需要拼接上 virtualhostName
queueName = virtualhostName + queueName;
exchangeName = virtualhostName + exchangeName;
try {
// 1. 判定 binding 是否存在
Binding existsBinding = memoryDataCenter.getBinding(queueName,
exchangeName);
if (existsBinding != null) {
throw new MqException ("[VirtualHost] binding 已经存在! queueName="
+ queueName + ", exchangeName=" + exchangeName);
}
// 2. 校验 bindingKey 是否合法
if (!router.checkBindingKeyValid(bindingKey)) {
throw new MqException ("[VirtualHost] bindingKey ⾮法! bindingKey="
+ bindingKey);
}
// 3. 创建 binding 对象
Binding binding = new Binding();
binding.setQueueName(queueName);
binding.setExchangeName(exchangeName);
binding.setBindingKey(bindingKey);
// 4. 获取到对应的 exchange 和 queue 对象
MSGQueue queue = memoryDataCenter.getQueue(queueName);
if (queue == null) {
throw new MqException ("[VirtualHost] 对应的队列不存在! queueName=" +
queueName);
}
Exchange exchange = memoryDataCenter.getExchange(exchangeName);
if (exchange == null) {
throw new MqException ("[VirtualHost] 对应的交换机不存在!
exchangeName=" + exchangeName);
}
// 5. 如果 exchange 和 queue 都是持久化的, 则 binding 也持久化.
if (queue.isDurable() && exchange.isDurable()) {
diskDataCenter.insertBinding(binding);
}
// 6. 写⼊内存
memoryDataCenter.insertBinding(binding);
System.out.println( "[VirtualHost] 创建绑定成功! exchangeName=" +
exchangeName + ", queueName=" + queueName);
return true;
} catch (Exception e) {
System.out.println( "[VirtualHost] 创建绑定失败! exchangeName=" +
exchangeName + ", queueName=" + queueName);
e.printStackTrace();2
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
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40

return false;
}
}41
42
43
删除绑定
// 解除绑定
public boolean queueUnbind (String queueName, String exchangeName) {
// 真实的 queueName 需要拼接上 virtualhostName
queueName = virtualhostName + queueName;
exchangeName = virtualhostName + exchangeName;
try {
// 1. 获取到 binding
Binding binding = memoryDataCenter.getBinding(queueName, exchangeName);
if (binding == null) {
throw new Exception ("[VirtualHost] 绑定不存在!");
}
// 2. 获取到对应的 exchange 和 queue 对象
MSGQueue queue = memoryDataCenter.getQueue(queueName);
if (queue == null) {
throw new Exception ("[VirtualHost] 对应的队列不存在! queueName=" +
queueName);
}
Exchange exchange = memoryDataCenter.getExchange(exchangeName);
if (exchange == null) {
throw new Exception ("[VirtualHost] 对应的交换机不存在! exchangeName="
+ exchangeName);
}
// 3. 如果 exchange 和 queue 都是持久化的, 则 binding 从硬盘删除
if (queue.isDurable() && exchange.isDurable()) {
diskDataCenter.deleteBinding(binding);
}
// 4. 从内存删除 binding
memoryDataCenter.deleteBinding(binding);
System.out.println( "[VirtualHost] 绑定删除成功! exchangeName=" +
exchangeName + ", queueName=" + queueName);
return true;
} catch (Exception e) {
System.out.println( "[VirtualHost] 绑定删除失败! exchangeName=" +
exchangeName + ", queueName=" + queueName);
e.printStackTrace();
return false;
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
21
22
23
24
25
26
27
28
29
30
31
32
33

}34
发布消息
•发布消息其实是把消息发送给指定的Exchange, 再根据Exchange 和Queue 的Binding 关系,转发到对应队列中.
•发送消息需要指定routingKey, 这个值的作⽤和ExchangeType 是相关的.
◦Direct: routingKey 就是对应队列的名字.此时不需要binding 关系,也不需要bindingKey, 就可以直接转发消息.
◦Fanout: routingKey 不起作⽤,bindingKey 也不起作⽤.此时消息会转发给绑定到该交换机上的所有队列中.
◦Topic: routingKey 是⼀个特定的字符串,会和bindingKey 进⾏匹配.如果匹配成功,则发到对应的队列中.具体规则后续介绍.
•BasicProperties 是消息的元信息.body 是消息本体.
// 发送消息
public boolean basicPublish (String exchangeName, String routingKey,
BasicProperties basicProperties, byte[] body) {
try {
// 1. 转换交换机名字. 如果是 null, 则使⽤默认交换机
if (exchangeName == null) {
exchangeName = "";
}
exchangeName = virtualhostName + exchangeName;
// 2. 检查参数合法性
if (!router.checkRoutingKeyValid(routingKey)) {
throw new MqException ("[VirtualHost] routingKey ⾮法! routingKey="
+ routingKey);
}
// 3. 查找到交换机对象
Exchange exchange = memoryDataCenter.getExchange(exchangeName);
if (exchange == null) {
throw new MqException ("[VirtualHost] 交换机不存在! exchangeName=" +
exchangeName);
}
if (exchange.getType() == ExchangeType.DIRECT) {
String queueName = virtualhostName + routingKey;1
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
21
22
23

// 4. 构造消息对象
Message message = Message.createMessageWithId(routingKey,
basicProperties, body);
// 5. 直接转发, 不需要 binding, 直接根据 routingKey 找到队列名, 进⾏转发.
MSGQueue queue = memoryDataCenter.getQueue(queueName);
if (queue == null) {
throw new MqException ("[VirtualHost] 队列不存在! queueName=" +
queueName);
}
// 6. 直接转发消息
sendMessage(queue, message);
} else {
// 4. 找到交换机对应的绑定对象
Map<String, Binding> bindings =
memoryDataCenter.getBindingsByExchange(exchangeName);
// 5. 遍历所有绑定, 进⼊消息转发逻辑.
for (Map.Entry<String, Binding> entry : bindings.entrySet()) {
// 1) 判定队列是否存在
Binding binding = entry.getValue();
MSGQueue queue =
memoryDataCenter.getQueue(binding.getQueueName());
if (queue == null) {
throw new MqException ("[VirtualHost] 队列不存在! queueName="
+ binding.getQueueName());
}
// 2) 构造消息对象. 针对每次写⼊队列, 都构造⼀个唯⼀的消息对象 id. 使同⼀个消息, 在不同队列中也能有不同的消息 id.
// 如果两个队列中的消息 id ⼀样, 此时就可能在 messageMap 中只存在
⼀份消息, ⽽在 queueMessageMap 中存在多份消息.
// 此时针对消息进⾏消费操作, 就可能出现⼀个队列消费了之后, 把消息从
messageMap 删除了; 第⼆次再从另⼀个队列消费
// 的时候, 就⽆法从 messageMap 中获取到消息了.
Message message = Message.createMessageWithId(routingKey,
basicProperties, body);
// 3) 判定能否转发
if (!router.route(exchange.getType(), binding, message)) {
continue ;
}
// 4) 真正转发消息
sendMessage(queue, message);
}
}
return true;
} catch (Exception e) {
System.out.println( "[VirtualHost] 消息发布失败!");24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60

e.printStackTrace();
return false;
}
}61
62
63
64
private void sendMessage (MSGQueue queue, Message message) throws Exception {
// 1. 先写硬盘
// deliverMode 为 1, 表⽰不持久化; 为 2 表⽰持久化. AMQP 协议规定的.
int deliveryMode = message.getBasicProperties().getDeliveryMode();
if (deliveryMode == 2) {
diskDataCenter.sendMessage(queue, message);
}
// 2. 再写内存
memoryDataCenter.sendMessage(queue, message);
// 3. 通知消费者去取消息
consumerManager.notifyConsume(queue.getName());
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
路由规则实现mqserver.core.Router
1)实现route ⽅法
public class Router {
public boolean route(ExchangeType exchangeType, Binding binding, Message
message) throws MqException {
// 根据不同的 exchangeType 进⾏不同的转发逻辑
// DIRECT 的转发逻辑已经在外部判定过.
if (exchangeType == ExchangeType.FANOUT) {
return routeFanout(binding, message);
} else if (exchangeType == ExchangeType.TOPIC) {
return routeTopic(binding, message);
} else {
throw new MqException ("[VirtualHost] 未知的 exchangeType!
exchangeType=" + exchangeType);
}
}
private boolean routeFanout (Binding binding, Message message) {1
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

// 对于 fanout 类型, 直接转发, 不需要进⾏任何匹配.
return true;
}
}15
16
17
18
2)实现checkRoutingKeyValid
⼀个RoutingKey 是由数字字⺟下划线构成的,并且可以使⽤.分成若⼲部分.
形如aaa.bbb.ccc
// 不包含通配符, 规则更简单.
public boolean checkRoutingKeyValid (String routingKey) {
if (routingKey.length() == 0) {
return true;
}
// 数字字⺟下划线构成
for (int i = 0; i < routingKey.length(); i++) {
char ch = routingKey.charAt(i);
if (ch >= 'A' && ch <= 'Z') {
continue ;
}
if (ch >= 'a' && ch <= 'z') {
continue ;
}
if (ch >= '0' && ch <= '9') {
continue ;
}
if (ch == '_' || ch == '.') {
continue ;
}
return false;
}
return true;
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
21
22
23
24
3)实现checkBindingKeyValid
⼀个BindingKey 是由数字字⺟下划线构成的,并且使⽤.分成若⼲部分.
另外,⽀持*和#两种通配符.(*#只能作为.切分出来的独⽴部分,不能和其他数字字⺟混⽤,⽐如
a. *.b 是合法的,a. *a.b 是不合法的).

其中*可以匹配任意⼀个单词.
其中#可以匹配任意零个或者多个单词.
例如:
bindingKey 为a. *.b, 可以匹配routingKey 为a.a.b 和a.b.b 和a.aaa.b
bindingKey 为a.#.b, 可以匹配routingKey 为a.a.b 和a.b.b 和a.aaa.b 和a.aa.bb.b 和a.b
// 需要考虑通配符, 复杂⼀些
public boolean checkBindingKeyValid (String bindingKey) {
// 1. 允许是空字符串
// 2. 数字字⺟下划线构成
// 3. 可以包含通配符
// 4. # 不能连续出现.
// 5. # 和 * 不能相邻
if (bindingKey.length() == 0) {
return true;
}
// 先判定基础构成
for (int i = 0; i < bindingKey.length(); i++) {
char ch = bindingKey.charAt(i);
if (ch >= 'A' && ch <= 'Z') {
continue ;
}
if (ch >= 'a' && ch <= 'z') {
continue ;
}
if (ch >= '0' && ch <= '9') {
continue ;
}
if (ch == '.' || ch == '_' || ch == '*' || ch == '#') {
continue ;
}
return false;
}
// 再判定每个词的情况
// ⽐如 aaa.a*a 这种应该视为⾮法.
String[] words = bindingKey.split( "\\.");
for (String word : words) {
if (word.length() > 1 && (word.contains( "*") ||
word.contains( "#"))) {
return false;
}
}
// 再判定相邻词的情况
for (int i = 0; i < words.length - 1; i++) {1
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
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37

// 连续两个 ##
if (words[i].equals( "#") && words[i + 1].equals( "#")) {
return false;
}
// # 连着 *
if (words[i].equals( "#") && words[i + 1].equals( "*")) {
return false;
}
// * 连着 #
if (words[i].equals( "*") && words[i + 1].equals( "#")) {
return false;
}
}
return true;
}38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
4)实现routeTopic
// 需要按照通配符匹配
// binding key 包含通配符
// 1. * 表⽰任意⼀个 token 都可以匹配
// 2. # 表⽰任意 0 个或 N 个 token 都可以匹配
// 3. 其他内容则要求严格匹配.
// 4. # 不会连续出现. # 和 * 不会相邻.
// routing key 不包含通配符. 这个在发消息的时候校验
private boolean routeTopic (Binding binding, Message message) {
// 按照 . 来切分 binding key 和 routing key
String[] bindingTokens = binding.getBindingKey().split( "\\.");
String[] routingTokens = message.getRoutingKey().split( "\\.");
// 使⽤双指针的⽅式来实现匹配
// 1. 如果是普通字符, 直接匹配内容是否相等, 不相等则返回 false, 相等直接进⼊下⼀轮
// 2. 如果是 * , 直接进⼊下⼀轮
// 3. 如果 # 没有下⼀个位置, 则直接返回 true
// 4. 如果遇到 # , 则找到 # 下⼀个位置的 token 在 routingKey 中的位置.
// 5. 如果能找到对应的位置了, 就可以继续匹配. 如果找不到, 就返回 false
// 6. 循环结束后, 检查看两个下标是否同时到达末尾. 是则匹配成功, 否则匹配失败.
int bindingIndex = 0;
int routingIndex = 0;
while (bindingIndex < bindingTokens.length && routingIndex <
routingTokens.length) {
if (bindingTokens[bindingIndex].equals( "*")) {
// 2. 如果是 * , 直接进⼊下⼀轮
// 直接进⼊下⼀轮⽐较 1
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
21
22
23
24

bindingIndex++;
routingIndex++;
} else if (bindingTokens[bindingIndex].equals( "#")) {
bindingIndex++;
if (bindingIndex == bindingTokens.length) {
// 3. 如果 # 没有下⼀个位置, 则直接返回 true
return true;
}
// 4. 如果遇到 # , 则找到 # 下⼀个位置的 token 在 routingKey 中的位置.
routingIndex = findNextMatch(routingTokens, routingIndex,
bindingTokens[bindingIndex]);
// 5. 如果能找到对应的位置了, 就可以继续下⼀轮匹配. 如果找不到, 就返回
false
if (routingIndex == - 1) {
return false;
}
bindingIndex++;
routingIndex++;
} else {
// 1. 如果是普通字符, 直接匹配内容是否相等, 不相等则返回 false, 相等直接进
⼊下⼀轮
if
(!bindingTokens[bindingIndex].equals(routingTokens[routingIndex])) {
return false;
}
bindingIndex++;
routingIndex++;
}
}
// 如果两⽅不能同时结束, 则也视为匹配失败.
// ⽐如 aaa.*.bbb 和 aaa.bbb
if (bindingIndex == bindingTokens.length && routingIndex ==
routingTokens.length) {
return true;
}
return false;
}
private int findNextMatch (String[] routingTokens, int routingIndex, String
bindingToken) {
for (int i = routingIndex; i < routingTokens.length; i++) {
if (routingTokens[i].equals(bindingToken)) {
return i;
}
}
return -1;25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65

}66
5)匹配规则测试⽤例
// [测试⽤例]
// binding key routing key result
// aaa aaa true
// aaa.bbb aaa.bbb true
// aaa.bbb aaa.bbb.ccc false
// aaa.bbb aaa.ccc false
// aaa.bbb.ccc aaa.bbb.ccc true
// aaa.* aaa.bbb true
// aaa.*.bbb aaa.bbb.ccc false
// *.aaa.bbb aaa.bbb false
// # aaa.bbb.ccc true
// aaa.# aaa.bbb true
// aaa.# aaa.bbb.ccc true
// aaa.#.ccc aaa.ccc true
// aaa.#.ccc aaa.bbb.ccc true
// aaa.#.ccc aaa.aaa.bbb.ccc true
// #.ccc ccc true
// #.ccc aaa.bbb.ccc true1
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
6)测试Router
创建RouterTests
@SpringBootTest
public class RouterTests {
private Router router = new Router();
private Message message = null;
private Binding binding = null;
@BeforeEach
public void setUp() {
message = new Message();
binding = new Binding();
}
@AfterEach1
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

public void tearDown () {
message = null;
binding = null;
}
}14
15
16
17
18
@Test
public void test() throws MqException {
binding.setBindingKey( "aaa");
message.setRoutingKey( "aaa");
Assertions.assertTrue(router.route(ExchangeType.TOPIC, binding, message));
binding.setBindingKey( "aaa.bbb" );
message.setRoutingKey( "aaa.bbb" );
Assertions.assertTrue(router.route(ExchangeType.TOPIC, binding, message));
binding.setBindingKey( "aaa.bbb" );
message.setRoutingKey( "aaa.bbb.ccc" );
Assertions.assertFalse(router.route(ExchangeType.TOPIC, binding, message));
binding.setBindingKey( "aaa.bbb" );
message.setRoutingKey( "aaa.ccc" );
Assertions.assertFalse(router.route(ExchangeType.TOPIC, binding, message));
binding.setBindingKey( "aaa.bbb.ccc" );
message.setRoutingKey( "aaa.bbb.ccc" );
Assertions.assertTrue(router.route(ExchangeType.TOPIC, binding, message));
binding.setBindingKey( "aaa.*");
message.setRoutingKey( "aaa.bbb" );
Assertions.assertTrue(router.route(ExchangeType.TOPIC, binding, message));
binding.setBindingKey( "aaa.*.bbb" );
message.setRoutingKey( "aaa.bbb.ccc" );
Assertions.assertFalse(router.route(ExchangeType.TOPIC, binding, message));
binding.setBindingKey( "*.aaa.bbb" );
message.setRoutingKey( "aaa.bbb" );
Assertions.assertFalse(router.route(ExchangeType.TOPIC, binding, message));
binding.setBindingKey( "#");
message.setRoutingKey( "aaa.bbb.ccc" );
Assertions.assertTrue(router.route(ExchangeType.TOPIC, binding, message));
binding.setBindingKey( "aaa.#");1
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
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39

message.setRoutingKey( "aaa.bbb" );
Assertions.assertTrue(router.route(ExchangeType.TOPIC, binding, message));
binding.setBindingKey( "aaa.#");
message.setRoutingKey( "aaa.bbb.ccc" );
Assertions.assertTrue(router.route(ExchangeType.TOPIC, binding, message));
binding.setBindingKey( "aaa.#.ccc" );
message.setRoutingKey( "aaa.ccc" );
Assertions.assertTrue(router.route(ExchangeType.TOPIC, binding, message));
binding.setBindingKey( "aaa.#.ccc" );
message.setRoutingKey( "aaa.bbb.ccc" );
Assertions.assertTrue(router.route(ExchangeType.TOPIC, binding, message));
binding.setBindingKey( "aaa.#.ccc" );
message.setRoutingKey( "aaa.aaa.bbb.ccc" );
Assertions.assertTrue(router.route(ExchangeType.TOPIC, binding, message));
binding.setBindingKey( "#.ccc");
message.setRoutingKey( "ccc");
Assertions.assertTrue(router.route(ExchangeType.TOPIC, binding, message));
binding.setBindingKey( "#.ccc");
message.setRoutingKey( "aaa.bbb.ccc" );
Assertions.assertTrue(router.route(ExchangeType.TOPIC, binding, message));
}40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
订阅消息
1)添加⼀个订阅者
// 订阅消息
// 如果是多个消费者消费⼀个队列, 将使⽤轮询的⽅式进⾏消费.
// 参数的 consumerTag 应该在⽹络通信部分设定.
public boolean basicConsume (String consumerTag, String queueName, boolean
autoAck, Consumer consumer) {
queueName = virtualhostName + queueName;
try {
// 把 consumer 加到监听线程管理的消费者数组中
consumerManager.addConsumer(consumerTag, queueName, autoAck, consumer);
System.out.println( "[VirtualHost] basicConsume 成功! queueName=" +
queueName);1
2
3
4
5
6
7
8
9

return true;
} catch (Exception e) {
System.out.println( "[VirtualHost] basicConsume 失败! queueName=" +
queueName);
e.printStackTrace();
return false;
}
}10
11
12
13
14
15
16
Consumer 相当于⼀个回调函数.放到common.Consumer 中.
@FunctionalInterface
public interface Consumer {
// consumerTag 消费者标识, 后⾯使⽤ channelId 填充.
void handleDelivery (String consumerTag, BasicProperties properties, byte[]
body) throws MqException, IOException;
}1
2
3
4
5
2)创建订阅者管理管理类创建mqserver.core.ConsumerManager
public class ConsumerManager {
private VirtualHost parent;
// 存放令牌的队列. 通过令牌来触发消费线程的消费操作.
private BlockingQueue<String> tokenQueue = new LinkedBlockingQueue <>();
private ExecutorService workerPool = Executors.newFixedThreadPool( 4);
}1
2
3
4
5
6
•parent ⽤来记录虚拟主机.
•使⽤⼀个阻塞队列⽤来触发消息消费.称为令牌队列.每次有消息过来了,都往队列中放⼀个令牌(也就是队列名),然后消费者再去消费对应队列的消息.
•使⽤⼀个线程池⽤来执⾏消息回调.
这样令牌队列的设定避免搞出来太多线程.否则就需要给每个队列都安排⼀个单独的线程了,如果队列很多则开销就⽐较⼤了.
3)添加令牌接⼝

// 通知消费者去消费消息
public void notifyConsume (String queueName) throws InterruptedException {
tokenQueue.put(queueName);
}1
2
3
4
4)实现添加订阅者
•新来订阅者的时候,需要先消费掉之前积压的消息.
•consumeMessage 真正的消息消费操作,⼀会再实现.
public void addConsumer (String consumerTag, String queueName, boolean autoAck,
Consumer consumer) throws MqException {
// 消费已经积压的消息消息
MSGQueue msgQueue = parent.getMemoryDataCenter().getQueue(queueName);
if (msgQueue == null) {
throw new MqException ("[ConsumerManager] 队列不存在! queueName=" +
queueName);
}
ConsumerEnv consumerEnv = new ConsumerEnv (consumerTag, queueName, autoAck,
consumer);
synchronized (msgQueue) {
msgQueue.addConsumerEnv(consumerEnv);
// 把已经积压的 n 个数据都先消费掉
int n = parent.getMemoryDataCenter().getMessageCount(queueName);
for (int i = 0; i < n; i++) {
consumeMessage(msgQueue);
}
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
创建ConsumerEnv ,这个类表⽰⼀个订阅者的执⾏环境.
// 表⽰⼀个消费者的上下⽂环境
public class ConsumerEnv {
private String consumerTag;
private String queueName;
private boolean autoAck;1
2
3
4
5

private Consumer consumer;
public ConsumerEnv (String consumerTag, String queueName, boolean autoAck,
Consumer consumer) {
this.consumerTag = consumerTag;
this.queueName = queueName;
this.autoAck = autoAck;
this.consumer = consumer;
}

// 省略 getter setter
}6
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
给MsgQueue 添加⼀个订阅者列表.
// 该队列被哪些消费者订阅
private List<ConsumerEnv> consumerEnvList = new ArrayList <>();
// 轮询序号
private AtomicInteger consumerSeq = new AtomicInteger (0);
public void addConsumerEnv (ConsumerEnv consumerEnv) {
consumerEnvList.add(consumerEnv);
}
public ConsumerEnv chooseConsumer () {
if (consumerEnvList.size() == 0) {
return null;
}
int index = consumerSeq.get() % consumerEnvList.size();
consumerSeq.getAndIncrement();
return consumerEnvList.get(index);
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
此处的chooseConsumer 是实现⼀个轮询效果.如果⼀个队列有多个订阅者,将会按照轮询的⽅式轮流拿到消息.
5)实现扫描线程在ConsumerManager 中创建⼀个线程,不停的尝试扫描令牌队列.如果拿到了令牌,就真正触发消费消息操作.

public ConsumerManager (VirtualHost parent) {
this.parent = parent;
// 启动扫描线程
Thread scanThread = new Thread(() -> {
while (true) {
try {
// 1. 拿到令牌
String queueName = tokenQueue.take();
// 2. 找到队列
MSGQueue msgQueue =
parent.getMemoryDataCenter().getQueue(queueName);
if (msgQueue == null) {
throw new MqException ("[ConsumerManager] 队列不存在!
queueName=" + queueName);
}
// 3. 消费⼀个数据
synchronized (msgQueue) {
consumeMessage(msgQueue);
}
} catch (MqException | InterruptedException e) {
e.printStackTrace();
}
}
}, "scanThread" );
scanThread.start();
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
21
22
23
24
25
6)实现消费消息所谓的消费消息,其实就是调⽤消息的回调.并把消息删除掉.
private void consumeMessage (MSGQueue msgQueue) throws MqException {
// 1. 按照轮询⽅式, 先找个消费者出来
ConsumerEnv luckyDog = msgQueue.chooseConsumer();
if (luckyDog == null) {
// 如果当前还没有订阅者, 就先暂时不消费.
return;
}
// 2. 从指定队列中取⼀个元素
Message message =
parent.getMemoryDataCenter().pollMessage(msgQueue.getName());
if (message == null) {
return;1
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

}
System.out.println( "[ConsumerManager] 消息被成功消费! queueName=" +
msgQueue.getName() + ", messageId=" + message.getMessageId());
// 3. 丢到线程池中⼲活. 回调执⾏时间可能⽐较⻓. 不适合让扫描线程去调⽤.
workerPool.submit(() -> {
try {
// 1. 先把消息放到待确认队列中
// ( 这个逻辑必须放到执⾏回调前⾯. 如果是 autoAck false, 在回调内部会调
⽤ basicAck, 执⾏彻底删除. 需要先放到待确认队列, 才能彻底删除)
parent.getMemoryDataCenter().addMessageWaitAck(msgQueue.getName(),
message);
// 2. 调⽤消费者的回调. 如果回调抛出异常了, 则不会对消息进⾏任何 ack 操作.
// 相当于消息仍然处在待消费的状态.
luckyDog.getConsumer().handleDelivery(luckyDog.getConsumerTag(),
message.getBasicProperties(), message.getBody());
// 3. 如果消息是⾃动确认, 则可以直接把消息彻底删除了.
// ( 这个逻辑必须放到执⾏回调后⾯. 万⼀执⾏回调⼀半服务器崩溃, 这个消息仍然存在于硬盘上, 下次启动还可以被继续消费到)
if (luckyDog.isAutoAck()) {
// 则修改硬盘上的消息为 "⽆效". 同时删除内存中的消息
if (message.getDeliveryMode() == 2) {
parent.getDiskDataCenter().deleteMessage(msgQueue,
message);
}

parent.getMemoryDataCenter().removeMessageWaitAck(msgQueue.getName(),
message.getMessageId());

parent.getMemoryDataCenter().removeMessage(message.getMessageId());
}
} catch (MqException | IOException | ClassNotFoundException e) {
e.printStackTrace();
}
});
}12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
注意:⼀个队列可能有N个消费者,此处应该按照轮询的⽅式挑⼀个消费者进⾏消费.
⼩结
⼀.消费消息的两种典型情况
1)订阅者已经存在了,才发送消息这种直接获取队列的订阅者,从中按照轮询的⽅式挑⼀个消费者来调⽤回调即可.

2)消息先发送到队列了,订阅者还没到.
此时当订阅者到达,就快速把指定队列中的消息全都消费掉.
⼆.关于消息不丢失的论证每个消息在从内存队列中出队列时,都会先进⼊待确认中.
•如果autoAck 为true
消息被消费完毕后(执⾏完消息回调之后),再执⾏清除⼯作.
分别清除硬盘数据,待确认队列,消息中⼼.
•如果autoAck 为false
在回调内部,进⾏清除⼯作.
分别清除硬盘数据,待确认队列,消息中⼼.
1)执⾏消息回调的时候抛出异常此时消息仍然处在待确认队列中.
此时可以⽤⼀个线程扫描待确认队列,如果发现队列中的消息超时未确认,则放⼊死信队列.
死信队列咱们此处暂不实现.
2)执⾏消息回调的时候服务器宕机内存所有数据都没了,但是消息在硬盘上仍然存在.会在服务下次启动的时候,加载回内存.重新被消费到.
消息确认下列⽅法只是⼿动应答的时候才会使⽤.
应答成功,则把消息删除掉.
public boolean basicAck (String queueName, String messageId) {
queueName = virtualhostName + queueName;
try {
// 删除待 ack 队列中的数据
memoryDataCenter.removeMessageWaitAck(queueName, messageId);
// 删除硬盘上的数据
MSGQueue queue = memoryDataCenter.getQueue(queueName);1
2
3
4
5
6
7

Message message = memoryDataCenter.getMessage(messageId);
if (message.getDeliveryMode() == 2) {
diskDataCenter.deleteMessage(queue, message);
}
// 删除内存中的数据
memoryDataCenter.removeMessage(messageId);
System.out.println( "[VirtualHost] basicAck 成功! queueName=" +
queueName + ", messageId=" + messageId);
return true;
} catch (Exception e) {
System.out.println( "[VirtualHost] basicAck 失败! queueName=" +
queueName + ", messageId=" + messageId);
e.printStackTrace();
}
return false;
}8
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
21
对于RabbitMQ 来说,还⽀持否定应答的情况.此处没有⽀持.同学们可以⾃⾏尝试实现.
测试VirtualHost
编写VirtualHostTests
•操作数据库,需要先启动Spring 服务.
•同时,需要先关闭Spring 服务,才能删除数据库⽂件
•使⽤FileUtils.deleteDirector 递归的删除⽬录中的内容.这个是Spring ⾃带的类
org.apache.tomcat.util.http.fileupload.FileUtils
@SpringBootTest
public class VirtualHostTests {
private VirtualHost virtualHost = null;
@BeforeEach
public void setUp() {
JavaMessageQueueApplication.ac =
SpringApplication.run(JavaMessageQueueApplication.class);
virtualHost = new VirtualHost ("");
}
@AfterEach
public void tearDown () throws IOException {
JavaMessageQueueApplication.ac.close();
File dbFile = new File("meta.db" );1
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

dbFile.delete();
File dataFile = new File("./data" );
FileUtils.deleteDirectory(dataFile);
}
}15
16
17
18
19
编写测试⽤例
@Test
public void testExchangeDeclare () {
boolean ok = virtualHost.exchangeDeclare( "testExchange" ,
ExchangeType.DIRECT, true, false, null);
Assertions.assertTrue(ok);
}
@Test
public void testExchangeDelete () {
boolean ok = virtualHost.exchangeDeclare( "testExchange" ,
ExchangeType.DIRECT, true, false, null);
Assertions.assertTrue(ok);
ok = virtualHost.exchangeDelete( "testExchange" );
Assertions.assertTrue(ok);
}
@Test
public void testQueueDeclare () {
boolean ok = virtualHost.queueDeclare( "testQueue" , true, false, false,
null);
Assertions.assertTrue(ok);
}
@Test
public void testQueueDelete () {
boolean ok = virtualHost.queueDeclare( "testQueue" , true, false, false,
null);
Assertions.assertTrue(ok);
ok = virtualHost.queueDelete( "testQueue" );
Assertions.assertTrue(ok);
}
@Test
public void testQueueBind () {
boolean ok = virtualHost.queueDeclare( "testQueue" , true, false, false,
null);
Assertions.assertTrue(ok);1
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
21
22
23
24
25
26
27
28
29
30
31
32

ok = virtualHost.exchangeDeclare( "testExchange" , ExchangeType.DIRECT,
true, false, null);
Assertions.assertTrue(ok);
ok = virtualHost.queueBind( "testQueue" , "testExchange" , "testBindingKey" );
Assertions.assertTrue(ok);
}
@Test
public void testQueueUnbind () {
boolean ok = virtualHost.queueDeclare( "testQueue" , true, false, false,
null);
Assertions.assertTrue(ok);
ok = virtualHost.exchangeDeclare( "testExchange" , ExchangeType.DIRECT,
true, false, null);
Assertions.assertTrue(ok);
ok = virtualHost.queueBind( "testQueue" , "testExchange" , "testBindingKey" );
Assertions.assertTrue(ok);
ok = virtualHost.queueUnbind( "testQueue" , "testExchange" );
Assertions.assertTrue(ok);
}
@Test
public void testBasicPublic () {
boolean ok = virtualHost.queueDeclare( "testQueue" , true, false, false,
null);
Assertions.assertTrue(ok);
ok = virtualHost.exchangeDeclare( "testExchange" , ExchangeType.DIRECT,
true, false, null);
Assertions.assertTrue(ok);
ok = virtualHost.basicPublish( "testExchange" , "testQueue" , null,
"hello".getBytes());
Assertions.assertTrue(ok);
}
// 先订阅消息, 后发送消息
@Test
public void testBasicConsumeDirect1 () throws InterruptedException {
boolean ok = virtualHost.queueDeclare( "testQueue" , true, false, false,
null);
Assertions.assertTrue(ok);
ok = virtualHost.exchangeDeclare( "testExchange" , ExchangeType.DIRECT,
true, false, null);
Assertions.assertTrue(ok);
ok = virtualHost.basicConsume( "testConsumerTag" , "testQueue" , true, new
Consumer () {33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70

@Override
public void handleDelivery (String consumerTag, BasicProperties
properties, byte[] body) throws MqException, IOException {
System.out.println( "messageId=" + properties.getMessageId());
Assertions.assertEquals( "testQueue" , properties.getRoutingKey());
Assertions.assertEquals( 1, properties.getDeliveryMode());
Assertions.assertArrayEquals( "hello".getBytes(), body);
}
});
Assertions.assertTrue(ok);
ok = virtualHost.basicPublish( "testExchange" , "testQueue" , null,
"hello".getBytes());
Assertions.assertTrue(ok);
}
// 先发送消息, 后订阅
@Test
public void testBasicConsumeDirect2 () throws InterruptedException {
boolean ok = virtualHost.queueDeclare( "testQueue" , true, false, false,
null);
Assertions.assertTrue(ok);
ok = virtualHost.exchangeDeclare( "testExchange" , ExchangeType.DIRECT,
true, false, null);
Assertions.assertTrue(ok);
ok = virtualHost.basicPublish( "testExchange" , "testQueue" , null,
"hello".getBytes());
Assertions.assertTrue(ok);
ok = virtualHost.basicConsume( "testConsumerTag" , "testQueue" , true, new
Consumer () {
@Override
public void handleDelivery (String consumerTag, BasicProperties
properties, byte[] body) throws MqException, IOException {
System.out.println( "messageId=" + properties.getMessageId());
Assertions.assertEquals( "testQueue" , properties.getRoutingKey());
Assertions.assertEquals( 1, properties.getDeliveryMode());
Assertions.assertArrayEquals( "hello".getBytes(), body);
}
});
Assertions.assertTrue(ok);
// 保证消费者有⾜够的时间完成消费
Thread.sleep( 500);
}
@Test71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110

public void testBasicConsumeFanout () throws InterruptedException {
boolean ok = virtualHost.exchangeDeclare( "testExchange" ,
ExchangeType.FANOUT, true, false, null);
Assertions.assertTrue(ok);
ok = virtualHost.queueDeclare( "testQueue1" , true, false, false, null);
Assertions.assertTrue(ok);
ok = virtualHost.queueBind( "testQueue1" , "testExchange" , "");
Assertions.assertTrue(ok);
ok = virtualHost.queueDeclare( "testQueue2" , true, false, false, null);
Assertions.assertTrue(ok);
ok = virtualHost.queueBind( "testQueue2" , "testExchange" , "");
Assertions.assertTrue(ok);
ok = virtualHost.basicPublish( "testExchange" , "", null,
"hello".getBytes());
Assertions.assertTrue(ok);
ok = virtualHost.basicConsume( "testConsumerTag" , "testQueue1" , false, new
Consumer () {
@Override
public void handleDelivery (String consumerTag, BasicProperties
properties, byte[] body) throws MqException, IOException {
System.out.println( "messageId=" + properties.getMessageId());
Assertions.assertEquals( "testQueue1" , properties.getRoutingKey());
Assertions.assertEquals( 1, properties.getDeliveryMode());
Assertions.assertArrayEquals( "hello".getBytes(), body);
}
});
Assertions.assertTrue(ok);
ok = virtualHost.basicConsume( "testConsumerTag" , "testQueue2" , true, new
Consumer () {
@Override
public void handleDelivery (String consumerTag, BasicProperties
properties, byte[] body) throws MqException, IOException {
System.out.println( "messageId=" + properties.getMessageId());
Assertions.assertEquals( "testQueue2" , properties.getRoutingKey());
Assertions.assertEquals( 1, properties.getDeliveryMode());
Assertions.assertArrayEquals( "hello".getBytes(), body);
}
});
Assertions.assertTrue(ok);
Thread.sleep( 500);
}111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151

@Test
public void testBasicConsumeTopic () throws InterruptedException {
boolean ok = virtualHost.exchangeDeclare( "testExchange" ,
ExchangeType.TOPIC, true, false, null);
Assertions.assertTrue(ok);
ok = virtualHost.queueDeclare( "testQueue" , true, false, false, null);
Assertions.assertTrue(ok);
ok = virtualHost.queueBind( "testQueue" , "testExchange" , "aaa.*");
Assertions.assertTrue(ok);
ok = virtualHost.basicPublish( "testExchange" , "aaa.bbb" , null,
"hello".getBytes());
Assertions.assertTrue(ok);
ok = virtualHost.basicConsume( "testConsumerTag" , "testQueue" , true, new
Consumer () {
@Override
public void handleDelivery (String consumerTag, BasicProperties
properties, byte[] body) throws MqException, IOException {
System.out.println( "messageId=" + properties.getMessageId());
Assertions.assertEquals( "testQueue" , properties.getRoutingKey());
Assertions.assertEquals( 1, properties.getDeliveryMode());
Assertions.assertArrayEquals( "hello".getBytes(), body);
}
});
Assertions.assertTrue(ok);
Thread.sleep( 500);
}
@Test
public void testBasicAck () throws InterruptedException {
boolean ok = virtualHost.queueDeclare( "testQueue" , true, false, false,
null);
Assertions.assertTrue(ok);
ok = virtualHost.exchangeDeclare( "testExchange" , ExchangeType.DIRECT,
true, false, null);
Assertions.assertTrue(ok);
ok = virtualHost.basicPublish( "testExchange" , "testQueue" , null,
"hello".getBytes());
Assertions.assertTrue(ok);
Thread.sleep( 500);
ok = virtualHost.basicConsume( "testConsumerTag" , "testQueue" , false, new
Consumer () {152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190

@Override
public void handleDelivery (String consumerTag, BasicProperties
properties, byte[] body) throws MqException, IOException {
System.out.println( "messageId=" + properties.getMessageId());
Assertions.assertEquals( "testQueue" , properties.getRoutingKey());
Assertions.assertEquals( 1, properties.getDeliveryMode());
Assertions.assertArrayEquals( "hello".getBytes(), body);
System.out.println( "===================================" );
// ⼿动调⽤ ack
Assertions.assertTrue(virtualHost.basicAck( "testQueue" ,
properties.getMessageId()));
}
});
Assertions.assertTrue(ok);
Thread.sleep( 500);
}191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
⼗⼀.⽹络通信协议设计明确需求接下来需要考虑客⼾端和服务器之间的通信.回顾交互模型.
⽣产者和消费者都是客⼾端,都需要通过⽹络和Broker Server 进⾏通信.
此处我们使⽤TCP协议,来作为通信的底层协议.同时在这个基础上⾃定义应⽤层协议,完成客⼾端对服务器这边功能的远程调⽤.

要调⽤的功能有:
•创建channel
•关闭channel
•创建exchange
•删除exchange
•创建queue
•删除queue
•创建binding
•删除binding
•发送message
•订阅message
•发送ack
•返回message (服务器->客⼾端)
设计应⽤层协议使⽤⼆进制的⽅式设定协议.
因为Message 的消息体本⾝就是⼆进制的.因此不太⽅便使⽤json等⽂本格式的协议.
请求:
响应:

其中type 表⽰请求响应不同的功能.取值如下:
•0x1 创建channel
•0x2 关闭channel
•0x3 创建exchange
•0x4 销毁exchange
•0x5 创建queue
•0x6 销毁queue
•0x7 创建binding
•0x8 销毁binding
•0x9 发送message
•0xa 订阅message
•0xb 返回ack
•0xc 服务器给客⼾端推送的消息.(被订阅的消息)响应独有的.
其中payload 部分,会根据不同的type, 存在不同的格式.
对于请求来说,payload 表⽰这次⽅法调⽤的各种参数信息.
对于响应来说,payload 表⽰这次⽅法调⽤的返回值.
定义Request /Response
创建common.Request
public class Request {
private int type;
private int length;
private byte[] payload;
// 省略 getter setter
}1
2
3
4
5
6
创建common.Response
public class Response { 1

private int type;
private int length;
private byte[] payload;
// 省略 getter setter
}2
3
4
5
6
定义参数⽗类构造⼀个类表⽰⽅法的参数,作为Request 的payload.
不同的⽅法中,参数形态各异,但是有些信息是通⽤的,使⽤⼀个⽗类表⽰出来.具体每个⽅法的参数再通过继承的⽅式体现.
common.BasicArguments
public class BaseArguments implements Serializable {
// 表⽰⼀次请求/响应的唯⼀ id. ⽤来把响应和请求对上.
protected String rid;
protected String channelId;
// 省略 getter setter
}1
2
3
4
5
6
7
•此处的rid和channelId 都是基于UUID 来⽣成的.rid⽤来标识⼀个请求-响应.这⼀点在请求响应
⽐较多的时候⾮常重要.
定义返回值⽗类和参数同理,也需要构造⼀个类表⽰返回值,作为Response 的payload.
common.BasicReturns
public class BaseReturns implements Serializable {
// 表⽰⼀次请求/响应的唯⼀ id. ⽤来把响应和请求对上.
protected String rid;
protected String channelId;
protected boolean ok;

// 省略 getter setter
}1
2
3
4
5
6
7
8

定义其他参数类针对每个VirtualHost 提供的⽅法,都需要有⼀个类表⽰对应的参数.
1)ExchangeDeclareArguments
public class ExchangeDeclareArguments extends BaseArguments implements
Serializable {
private String exchangeName;
private ExchangeType exchangeType;
private boolean durable;
private boolean autoDelete;
private Map<String, Object> arguments;
}1
2
3
4
5
6
7
⼀个创建交换机的请求,形如:
•可以把ExchangeDeclareArguments 转成byte[], 就得到了下列图⽚的结构.
•按照length ⻓度读取出payload, 就可以把读到的⼆进制数据转换成
ExchangeDeclareArguments 对象.
后续请求报⽂格式同理,就不再重复画了.
2)ExchangeDeleteArguments
public class ExchangeDeleteArguments extends BaseArguments implements
Serializable {
private String exchangeName;1
2

}3
3)QueueDeclareArguments
public class QueueDeclareArguments extends BaseArguments implements
Serializable {
private String queueName;
private boolean durable;
private boolean exclusive;
private boolean autoDelete;
private Map<String, Object> arguments;
}1
2
3
4
5
6
7
4)QueueDeleteArguments
public class QueueDeleteArguments extends BaseArguments implements Serializable
{
private String queueName;
}1
2
3
5)QueueBindArguments
public class QueueBindArguments extends BaseArguments implements Serializable {
private String queueName;
private String exchangeName;
private String bindingKey;
}1
2
3
4
5
6)QueueUnbindArguments
public class QueueUnbindArguments extends BaseArguments implements Serializable
{
private String queueName;1
2

private String exchangeName;
}3
4
7)BasicPublishArguments
public class BasicPublishArguments extends BaseArguments implements
Serializable {
private String exchangeName;
private String routingKey;
private BasicProperties basicProperties;
private byte[] body;
}1
2
3
4
5
6
8)BasicConsumeArguments
public class BasicConsumeArguments extends BaseArguments implements
Serializable {
private String consumeTag;
private String queueName;
private boolean autoAck;
}1
2
3
4
5
9)SubScribeReturns
•这个不是参数,是返回值.是服务器给消费者推送的订阅消息.
•consumerTag 其实是channelId.
•basicProperties 和body 共同构成了Message.
public class SubScribeReturns extends BaseReturns implements Serializable {
private String consumerTag;
private BasicProperties basicProperties;
private byte[] body;
} 1
2
3
4
5

⼗⼆.实现BrokerServer
创建BrokerServer 类
public class BrokerServer {
// 当前程序只考虑⼀个虚拟主机的情况.
private VirtualHost virtualHost = new VirtualHost ("default-VirtualHost" );
// key 为 channelId, value 为 channel 对应的 socket 对象.
private ConcurrentHashMap<String, Socket> sessions = new
ConcurrentHashMap <>();
private ServerSocket serverSocket;
private ExecutorService executorService;
private volatile boolean runnable = true;
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
•virtualHost 表⽰服务器持有的虚拟主机.队列,交换机,绑定,消息都是通过虚拟主机管理.
•sessions ⽤来管理所有的客⼾端的连接.记录每个客⼾端的socket.
•serverSocket 是服务器⾃⾝的socket
•executorService 这个线程池⽤来处理响应.
•runnable 这个标志位⽤来控制服务器的运⾏停⽌.
启动/停⽌服务器
•这⾥就是⼀个单纯的TCP服务器,没啥特别的.
•实现停⽌操作,主要是为了⽅便后续开展单元测试.
public BrokerServer (int port) throws IOException {
serverSocket = new ServerSocket (port);
}
public void start() throws IOException {
System.out.println( "[BrokerServer] 启动完成!");
executorService = Executors.newCachedThreadPool();
try {
while (runnable) {
Socket clientSocket = serverSocket.accept();
executorService.submit(() -> processConnection(clientSocket));
}
} catch (SocketException e) {1
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

System.out.println( "[BrokerServer] 服务器关闭完成!");
}
}
public void stop() throws IOException {
runnable = false;
// ⽴即结束所有的线程池的任务
executorService.shutdownNow();
serverSocket.close();
}14
15
16
17
18
19
20
21
22
23
实现处理连接
•对于EOFException 和SocketException ,我们视为客⼾端正常断开连接.
◦如果是客⼾端先close, 后调⽤DataInputStream 的read, 则抛出EOFException
◦如果是先调⽤DataInputStream 的read, 后客⼾端调⽤close, 则抛出SocketException
private void processConnection (Socket clientSocket) {
try (InputStream inputStream = clientSocket.getInputStream();
OutputStream outputStream = clientSocket.getOutputStream()) {
DataInputStream dataInputStream = new DataInputStream (inputStream);
DataOutputStream dataOutputStream = new DataOutputStream (outputStream);
while (true) {
Request request = readRequest(dataInputStream);
Response response = process(request, clientSocket);
writeResponse(dataOutputStream, response);
}
} catch (EOFException | SocketException e) {
System.out.println( "[BrokerServer] connection 关闭! serverIP=" +
clientSocket.getInetAddress().toString()
+ ", port=" + clientSocket.getPort());
} catch (MqException | IOException | ClassNotFoundException e) {
System.out.println( "[BrokerServer] connection 出现异常!");
e.printStackTrace();
} finally {
try {
clientSocket.close();
// 对 sessions 进⾏清理
clearClosedSession(clientSocket);
} catch (IOException e) {
e.printStackTrace();
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
21
22
23
24

}
}25
26
实现readRequest
private Request readRequest (DataInputStream dataInputStream) throws
IOException {
Request request = new Request();
request.setType(dataInputStream.readInt());
request.setLength(dataInputStream.readInt());
byte[] payload = new byte[request.getLength()];
int n = dataInputStream.read(payload);
if (n != request.getLength()) {
throw new IOException ("读取请求数据出错!");
}
request.setPayload(payload);
return request;
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
实现writeResponse
•注意这⾥的flush 操作很关键,否则响应不⼀定能及时返回给客⼾端.
private void writeResponse (DataOutputStream dataOutputStream, Response
response) throws IOException {
dataOutputStream.writeInt(response.getType());
dataOutputStream.writeInt(response.getLength());
dataOutputStream.write(response.getPayload());
dataOutputStream.flush();
}1
2
3
4
5
6
实现处理请求
•先把请求转换成BaseArguments ,获取到其中的channelId 和rid
•再根据不同的type, 分别处理不同的逻辑.(主要是调⽤virtualHost 中不同的⽅法).

•针对消息订阅操作,则需要在存在消息的时候通过回调,把响应结果写回给对应的客⼾端.
•最后构造成统⼀的响应.
private Response process(Request request, Socket clientSocket) throws
MqException, IOException, ClassNotFoundException {
// 1. 从 request 中解析出业务请求
BaseArguments baseArguments = (BaseArguments)
BinaryTool.fromBytes(request.getPayload());
System.out.println( "[Request] rid=" + baseArguments.getRid() + ",
channelId=" + baseArguments.getChannelId()
+ ", type=" + request.getType() + ", length=" +
request.getLength());
// 2. 根据 type 来区分业务分⽀.
boolean ok = true;
if (request.getType() == 0x1) {
// 创建 channel
sessions.put(baseArguments.getChannelId(), clientSocket);
System.out.println( "[BrokerServer] 创建 channel 完成! channelId=" +
baseArguments.getChannelId());
} else if (request.getType() == 0x2) {
// 销毁 channel
sessions.remove(baseArguments.getChannelId());
System.out.println( "[BrokerServer] 销毁 channel 完成! channelId=" +
baseArguments.getChannelId());
} else if (request.getType() == 0x3) {
// 创建交换机
ExchangeDeclareArguments exchangeDeclareArguments =
(ExchangeDeclareArguments) baseArguments;
ok =
virtualHost.exchangeDeclare(exchangeDeclareArguments.getExchangeName(),
exchangeDeclareArguments.getExchangeType(),
exchangeDeclareArguments.isDurable(),
exchangeDeclareArguments.isAutoDelete(),
exchangeDeclareArguments.getArguments());
} else if (request.getType() == 0x4) {
// 删除交换机
ExchangeDeleteArguments exchangeDeleteArguments =
(ExchangeDeleteArguments) baseArguments;
ok =
virtualHost.exchangeDelete(exchangeDeleteArguments.getExchangeName());
} else if (request.getType() == 0x5) {
// 创建队列
QueueDeclareArguments queueDeclareArguments = (QueueDeclareArguments)
baseArguments;
ok = virtualHost.queueDeclare(queueDeclareArguments.getQueueName(),
queueDeclareArguments.isDurable(), queueDeclareArguments.isExclusive(),1
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
21
22
23
24
25
26
27
28

queueDeclareArguments.isAutoDelete(),
queueDeclareArguments.getArguments());
} else if (request.getType() == 0x6) {
// 删除队列
QueueDeleteArguments queueDeleteArguments = (QueueDeleteArguments)
baseArguments;
ok = virtualHost.queueDelete(queueDeleteArguments.getQueueName());
} else if (request.getType() == 0x7) {
// 创建绑定
QueueBindArguments queueBindArguments = (QueueBindArguments)
baseArguments;
ok = virtualHost.queueBind(queueBindArguments.getQueueName(),
queueBindArguments.getExchangeName(), queueBindArguments.getBindingKey());
} else if (request.getType() == 0x8) {
// 解除绑定
QueueUnbindArguments queueUnbindArguments = (QueueUnbindArguments)
baseArguments;
ok = virtualHost.queueUnbind(queueUnbindArguments.getQueueName(),
queueUnbindArguments.getExchangeName());
} else if (request.getType() == 0x9) {
// 发送消息
BasicPublishArguments basicPublishArguments = (BasicPublishArguments)
baseArguments;
ok = virtualHost.basicPublish(basicPublishArguments.getExchangeName(),
basicPublishArguments.getRoutingKey(),
basicPublishArguments.getBasicProperties(),
basicPublishArguments.getBody());
} else if (request.getType() == 0xa) {
// 订阅消息
BasicConsumeArguments basicConsumeArguments = (BasicConsumeArguments)
baseArguments;
// 创建个回调, ⽤来把消费的数据转发回客⼾端.
ok = virtualHost.basicConsume(basicConsumeArguments.getConsumeTag(),
basicConsumeArguments.getQueueName(),
basicConsumeArguments.isAutoAck(), new Consumer () {
@Override
public void handleDelivery (String consumerTag,
BasicProperties properties, byte[] body) throws MqException, IOException {
// 1. 根据 channelId 找到对应的 socket
Socket clientSocket =
sessions.get(basicConsumeArguments.getChannelId());
if (clientSocket == null || clientSocket.isClosed()) {
throw new MqException ("[BrokerServer] 订阅消息的客⼾
端已经关闭!");
}
// 2. 构造响应数据 29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60

SubScribeReturns subScribeReturns = new
SubScribeReturns ();

subScribeReturns.setChannelId(basicConsumeArguments.getChannelId());
subScribeReturns.setConsumerTag(consumerTag);
subScribeReturns.setBasicProperties(properties);
subScribeReturns.setBody(body);
byte[] payload = BinaryTool.toBytes(subScribeReturns);
// 3. 写⼊到对应 socket 中
Response response = new Response ();
response.setType( 0xc);
response.setLength(payload.length);
response.setPayload(payload);
// 此处不应该关闭 DataOutputStream, 关闭这个会导致内部持有的 clientSocket.getOutputStream 被关闭.
DataOutputStream dataOutputStream = new
DataOutputStream (clientSocket.getOutputStream());
writeResponse(dataOutputStream, response);
}
});
} else if (request.getType() == 0xb) {
// 确认 ack
BasicAckArguments basicAckArguments = (BasicAckArguments)
baseArguments;
ok = virtualHost.basicAck(basicAckArguments.getQueueName(),
basicAckArguments.getMessageId());
} else {
throw new MqException ("[BrokerServer] 未知的请求 type ! type=" +
request.getType());
}
// 3. 构造响应.
BaseReturns baseReturns = new BaseReturns ();
baseReturns.setRid(baseArguments.getRid());
baseReturns.setChannelId(baseArguments.getChannelId());
baseReturns.setOk(ok);
byte[] payload = BinaryTool.toBytes(baseReturns);
Response response = new Response ();
response.setType(request.getType());
response.setLength(payload.length);
response.setPayload(payload);
System.out.println( "[Response] rid=" + baseReturns.getRid() + ",
channelId=" + baseReturns.getChannelId()
+ ", type=" + response.getType() + ", length=" +
response.getLength());
return response;
}61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98

实现clearClosedSession
•如果客⼾端只关闭了Connection, 没关闭Connection 中包含的Channel, 也没关系,在这⾥统⼀进
⾏清理.
•注意迭代器失效问题.
private void clearClosedSession (Socket clientSocket) {
// 这⾥不要在同⼀个循环中, 同时进⾏遍历 + 删除操作. 否则可能有迭代器失效问题.
// 拆成两个循环来处理是更合适的.
List<String> toDeleteChannelId = new ArrayList <>();
for (Map.Entry<String, Socket> entry : sessions.entrySet()) {
if (entry.getValue() == clientSocket) {
toDeleteChannelId.add(entry.getKey());
}
}
for (String channelId : toDeleteChannelId) {
sessions.remove(channelId);
}
System.out.println( "[BrokerServer] 清理 session 完成! 被清理的 channelId=" +
toDeleteChannelId);
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
⼗三.实现客⼾端创建包mqclient
创建ConnectionFactory
⽤来创建连接的⼯⼚类.
•当前没有实现⽤⼾认证和多虚拟主机,⽤⼾名密码可以暂时先不要.
public class ConnectionFactory {
// BrokerServer 的 ip 和 port
private String host;
private int port;
// 这⼏个部分暂时不加.
// private String virtualHost;1
2
3
4
5
6

// private String username;
// private String password;
// 建⽴⼀个 tcp 连接
public Connection newConnection () throws IOException {
Connection connection = new Connection (host, port);
return connection;
}
}7
8
9
10
11
12
13
14
15
Connection 和Channel 的定义
⼀个客⼾端可以创建多个Connection.
⼀个Connection 对应⼀个socket, ⼀个TCP连接.
⼀个Connection 可以包含多个Channel
1)Connection 的定义
public class Connection {
private Socket socket;
private InputStream inputStream;
private OutputStream outputStream;
private DataInputStream dataInputStream;
private DataOutputStream dataOutputStream;
// 记录当前 Connection 包含的 Channel
private ConcurrentHashMap<String, Channel> channelMap = new
ConcurrentHashMap <>();
// 执⾏消费消息回调的线程池
private ExecutorService callbackPool = Executors.newFixedThreadPool( 4);
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
•Socket 是客⼾端持有的套接字.InputStream OutputStream DataInputStream
DataOutputStream 均为socket 通信的接⼝.
•channelMap ⽤来管理该连接中所有的Channel.
•callbackPool 是⽤来在客⼾端这边执⾏⽤⼾回调的线程池.
2)Channel 的定义

public class Channel {
private String channelId;
private Connection connection;
// key 为 rid, 即 requestId / responseId.
private ConcurrentHashMap<String, BaseReturns> baseReturnsMap = new
ConcurrentHashMap <>();
// 订阅消息的回调
private Consumer consumer = null;
public Channel(String channelId, Connection connection) {
this.channelId = channelId;
this.connection = connection;
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
•channelId 为channel 的⾝份标识,使⽤UUID 标识.
•Connection 为channel 对应的连接.
•baseReturnsMap ⽤来保存响应的返回值.放到这个哈希表中⽅便和请求匹配.
•consumer 为消费者的回调(⽤⼾注册的).对于消息响应,应该调⽤这个回调处理消息.
封装请求响应读写操作在Connection 中,实现下列⽅法
// 读取响应应该在另外⼀个单独的线程中完成.
public void writeRequest (Request request) throws IOException {
dataOutputStream.writeInt(request.getType());
dataOutputStream.writeInt(request.getLength());
dataOutputStream.write(request.getPayload());
dataOutputStream.flush();
System.out.println( "[Connection] 发送请求! type=" + request.getType() + ",
length=" + request.getLength());
}1
2
3
4
5
6
7
8
public Response readResponse () throws IOException {
Response response = new Response ();
response.setType(dataInputStream.readInt());
response.setLength(dataInputStream.readInt());
byte[] payload = new byte[response.getLength()];1
2
3
4
5

int n = dataInputStream.read(payload);
if (n != response.getLength()) {
throw new IOException ("读取到的响应数据不完整!");
}
response.setPayload(payload);
System.out.println( "[Connection] 收到响应! type=" + response.getType() + ",
length=" + response.getLength());
return response;
}6
7
8
9
10
11
12
13
创建channel
在Connection 中,定义下列⽅法来创建⼀个channel
public Channel createChannel () throws IOException {
// 使⽤ UUID ⽣产 channelId, 以 C- 开头
String channelId = "C-" + UUID.randomUUID().toString();
Channel channel = new Channel(channelId, this);
// 这⾥需要先把 channel 键值对放到 Map 中. 否则后续 createChannel 的阻塞等待就等不到结果了
channelMap.put(channelId, channel);
boolean ok = channel.createChannel();
if (!ok) {
// 服务器返回创建 channel 失败!
// 把 channelId 删除掉即可
channelMap.remove(channelId);
return null;
}
return channel;
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
发送请求通过Channel 提供请求的发送操作.
1)创建channel
public boolean createChannel () throws IOException { 1

BaseArguments baseArguments = new BaseArguments ();
baseArguments.setRid(generateRid());
baseArguments.setChannelId(channelId);
byte[] payload = BinaryTool.toBytes(baseArguments);
Request request = new Request();
request.setType( 0x1);
request.setLength(payload.length);
request.setPayload(payload);
connection.writeRequest(request);
// 阻塞等待服务器的响应
BaseReturns baseReturns = waitResult(baseArguments.getRid());
return baseReturns.isOk();
}2
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
generateRid 的实现
private String generateRid () {
return "R-" + UUID.randomUUID().toString();
}1
2
3
waitResult 的实现
•由于服务器的响应是异步的.此处通过waitResult 实现同步等待的效果.
private BaseReturns waitResult (String rid){
BaseReturns baseReturns = null;
while ((baseReturns = baseReturnsMap.get(rid)) == null) {
synchronized (this) {
try {
wait();
} catch (InterruptedException e) {
// 如果 wait 被提前唤醒, 也应该继续循环.
// 所以这⾥啥都不⼲, 但是 try 需要放到 while 内部.
e.printStackTrace();
}
}
}
return baseReturns;
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

2)关闭channel
public boolean close() throws IOException {
// 删除服务器上的 channel. 如果不显式调⽤, 也没关系. 服务器会在 Connection 断开的时候统⼀回收.
BaseArguments baseArguments = new BaseArguments ();
baseArguments.setRid(generateRid());
baseArguments.setChannelId(channelId);
byte[] payload = BinaryTool.toBytes(baseArguments);
Request request = new Request();
request.setType( 0x2);
request.setLength(payload.length);
request.setPayload(payload);
connection.writeRequest(request);
// 阻塞等待服务器的响应
BaseReturns baseReturns = waitResult(baseArguments.getRid());
return baseReturns.isOk();
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
3)创建交换机
public boolean exchangeDeclare (String exchangeName, ExchangeType exchangeType,
boolean durable, boolean autoDelete,
Map<String, Object> arguments) throws IOException {
ExchangeDeclareArguments exchangeDeclareArguments = new
ExchangeDeclareArguments ();
exchangeDeclareArguments.setRid(generateRid());
exchangeDeclareArguments.setChannelId(channelId);
exchangeDeclareArguments.setExchangeName(exchangeName);
exchangeDeclareArguments.setExchangeType(exchangeType);
exchangeDeclareArguments.setDurable(durable);
exchangeDeclareArguments.setAutoDelete(autoDelete);
exchangeDeclareArguments.setArguments(arguments);
byte[] payload = BinaryTool.toBytes(exchangeDeclareArguments);
Request request = new Request();
request.setType( 0x3);
request.setLength(payload.length);
request.setPayload(payload);
connection.writeRequest(request);1
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

// 阻塞等待服务器的响应
BaseReturns baseReturns = waitResult(exchangeDeclareArguments.getRid());
return baseReturns.isOk();
}18
19
20
21
22
4)删除交换机
public boolean exchangeDelete (String exchangeName) throws IOException {
ExchangeDeleteArguments exchangeDeleteArguments = new
ExchangeDeleteArguments ();
exchangeDeleteArguments.setRid(generateRid());
exchangeDeleteArguments.setChannelId(channelId);
exchangeDeleteArguments.setExchangeName(exchangeName);
byte[] payload = BinaryTool.toBytes(exchangeDeleteArguments);
Request request = new Request();
request.setType( 0x4);
request.setLength(payload.length);
request.setPayload(payload);
connection.writeRequest(request);
// 阻塞等待服务器的响应
BaseReturns baseReturns = waitResult(exchangeDeleteArguments.getRid());
return baseReturns.isOk();
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
5)创建队列
public boolean queueDeclare (String queueName, boolean durable, boolean
exclusive, boolean autoDelete,
Map<String, Object> arguments) throws IOException {
QueueDeclareArguments queueDeclareArguments = new QueueDeclareArguments ();
queueDeclareArguments.setRid(generateRid());
queueDeclareArguments.setChannelId(channelId);
queueDeclareArguments.setQueueName(queueName);
queueDeclareArguments.setDurable(durable);
queueDeclareArguments.setExclusive(exclusive);
queueDeclareArguments.setAutoDelete(autoDelete);1
2
3
4
5
6
7
8
9

queueDeclareArguments.setArguments(arguments);
byte[] payload = BinaryTool.toBytes(queueDeclareArguments);
Request request = new Request();
request.setType( 0x5);
request.setLength(payload.length);
request.setPayload(payload);
connection.writeRequest(request);
// 阻塞等待服务器的响应
BaseReturns baseReturns = waitResult(queueDeclareArguments.getRid());
return baseReturns.isOk();
}10
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
21
22
6)删除队列
public boolean queueDelete (String queueName) throws IOException {
QueueDeleteArguments queueDeleteArguments = new QueueDeleteArguments ();
queueDeleteArguments.setRid(generateRid());
queueDeleteArguments.setChannelId(channelId);
queueDeleteArguments.setQueueName(queueName);
byte[] payload = BinaryTool.toBytes(queueDeleteArguments);
Request request = new Request();
request.setType( 0x6);
request.setLength(payload.length);
request.setPayload(payload);
connection.writeRequest(request);
// 阻塞等待服务器的响应
BaseReturns baseReturns = waitResult(queueDeleteArguments.getRid());
return baseReturns.isOk();
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
7)创建绑定
// 对于直接交换机和 fanout 交换机, bindingKey 不⽣效. 直接设为 "" 即可
public boolean queueBind (String queueName, String exchangeName) throws
IOException {1
2

return queueBind(queueName, exchangeName, "");
}
public boolean queueBind (String queueName, String exchangeName, String
bindingKey) throws IOException {
QueueBindArguments queueBindArguments = new QueueBindArguments ();
queueBindArguments.setRid(generateRid());
queueBindArguments.setChannelId(channelId);
queueBindArguments.setQueueName(queueName);
queueBindArguments.setExchangeName(exchangeName);
queueBindArguments.setBindingKey(bindingKey);
byte[] payload = BinaryTool.toBytes(queueBindArguments);
Request request = new Request();
request.setType( 0x7);
request.setLength(payload.length);
request.setPayload(payload);
connection.writeRequest(request);
// 阻塞等待服务器的响应
BaseReturns baseReturns = waitResult(queueBindArguments.getRid());
return baseReturns.isOk();
}3
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
21
22
23
24
8)删除绑定
public boolean queueUnbind (String queueName, String exchangeName) throws
IOException {
QueueUnbindArguments queueUnbindArguments = new QueueUnbindArguments ();
queueUnbindArguments.setRid(generateRid());
queueUnbindArguments.setChannelId(channelId);
queueUnbindArguments.setQueueName(queueName);
queueUnbindArguments.setExchangeName(exchangeName);
byte[] payload = BinaryTool.toBytes(queueUnbindArguments);
Request request = new Request();
request.setType( 0x8);
request.setLength(payload.length);
request.setPayload(payload);
connection.writeRequest(request);
// 阻塞等待服务器的响应
BaseReturns baseReturns = waitResult(queueUnbindArguments.getRid());1
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

return baseReturns.isOk();
}17
18
9)发送消息
public boolean basicPublish (String exchangeName, String routingKey,
BasicProperties basicProperties, byte[] body) throws IOException {
BasicPublishArguments basicPublishArguments = new BasicPublishArguments ();
basicPublishArguments.setRid(generateRid());
basicPublishArguments.setChannelId(channelId);
basicPublishArguments.setExchangeName(exchangeName);
basicPublishArguments.setRoutingKey(routingKey);
basicPublishArguments.setBasicProperties(basicProperties);
basicPublishArguments.setBody(body);
byte[] payload = BinaryTool.toBytes(basicPublishArguments);
Request request = new Request();
request.setType( 0x9);
request.setLength(payload.length);
request.setPayload(payload);
connection.writeRequest(request);
// 阻塞等待服务器的响应
BaseReturns baseReturns = waitResult(basicPublishArguments.getRid());
return baseReturns.isOk();
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
10)订阅消息
public boolean basicConsume (String queueName, boolean autoAck, Consumer
consumer) throws IOException, MqException {
BasicConsumeArguments basicConsumeArguments = new BasicConsumeArguments ();
basicConsumeArguments.setRid(generateRid());
basicConsumeArguments.setChannelId(channelId);
basicConsumeArguments.setQueueName(queueName);
basicConsumeArguments.setAutoAck(autoAck);
basicConsumeArguments.setConsumeTag(channelId);
byte[] payload = BinaryTool.toBytes(basicConsumeArguments);1
2
3
4
5
6
7
8
9

Request request = new Request();
request.setType( 0xa);
request.setLength(payload.length);
request.setPayload(payload);
connection.writeRequest(request);
// 阻塞等待服务器的响应
BaseReturns baseReturns = waitResult(basicConsumeArguments.getRid());
if (baseReturns.isOk()) {
// 设置回调
if (this.consumer != null) {
throw new MqException ("该 channel 已经设置过消费回调, 不能重复设置!");
}
this.consumer = consumer;
}
return baseReturns.isOk();
}10
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
21
22
23
24
25
26
11)确认消息
public boolean basicAck (String queueName, String messageId) throws IOException
{
BasicAckArguments basicAckArguments = new BasicAckArguments ();
basicAckArguments.setRid(generateRid());
basicAckArguments.setChannelId(channelId);
basicAckArguments.setQueueName(queueName);
basicAckArguments.setMessageId(messageId);
byte[] payload = BinaryTool.toBytes(basicAckArguments);
Request request = new Request();
request.setType( 0xb);
request.setLength(payload.length);
request.setPayload(payload);
connection.writeRequest(request);
// 阻塞等待服务器的响应
BaseReturns baseReturns = waitResult(basicAckArguments.getRid());
return baseReturns.isOk();
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
⼩结

上述发送请求的操作,逻辑基本⼀致.构造参数+构造请求+发送+等待结果.
处理响应
1)创建扫描线程创建⼀个扫描线程,⽤来不停的读取socket 中的响应数据.
注意:⼀个Connection 中可能包含多个channel, 需要把响应分别放到对应的channel 中.
public Connection (String host, int port) throws IOException {
socket = new Socket(host, port);
inputStream = socket.getInputStream();
outputStream = socket.getOutputStream();
dataInputStream = new DataInputStream (inputStream);
dataOutputStream = new DataOutputStream (outputStream);
// 创建⼀个读响应的线程
Thread t = new Thread(() -> {
try {
while (!socket.isClosed()) {
Response response = readResponse();
dispatchResponse(response);
}
} catch (SocketException e) {
// 连接断开, 忽略该异常.
// System.out.println("[Connection] 连接断开!");
} catch (IOException | ClassNotFoundException | MqException e) {
System.out.println( "[Connection] 连接出现异常!");
e.printStackTrace();
}
});
t.start();
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
21
22
23
24
2)实现响应的分发给Connection 创建dispatchResponse ⽅法.
•针对服务器返回的控制响应和消息响应,分别处理.
◦如果是订阅数据,则调⽤channel 中的回调.

◦如果是控制消息,直接放到结果集合中.
private void dispatchResponse (Response response) throws IOException,
ClassNotFoundException, MqException {
if (response.getType() == 0xc) {
// 1. 解析到服务器返回的订阅数据
SubScribeReturns subScribeReturns = (SubScribeReturns)
BinaryTool.fromBytes(response.getPayload());
// 2. 获取到 channel
Channel channel = channelMap.get(subScribeReturns.getChannelId());
if (channel == null) {
throw new MqException ("该消息对应的 channel 不存在! channelId=" +
subScribeReturns.getChannelId());
}
// 3. 执⾏ channel 中对应的回调.
callbackPool.submit(() -> {
try {

channel.getConsumer().handleDelivery(subScribeReturns.getConsumerTag(),
subScribeReturns.getBasicProperties(),
subScribeReturns.getBody());
} catch (MqException | IOException e) {
e.printStackTrace();
}
});
} else {
// 1. 拿到服务器返回的控制消息
BaseReturns baseReturns = (BaseReturns)
BinaryTool.fromBytes(response.getPayload());
// System.out.printf("[Connection] 收到响应: type=0x%x, channelId=%s,
ok=%b\n", response.getType(),
// baseReturns.getChannelId(), baseReturns.isOk());
// 2. 找到对应 Channel
Channel channel = channelMap.get(baseReturns.getChannelId());
if (channel == null) {
// 这个是⼩问题, 不要抛异常
System.out.println( "[Connection] channel 不存在! channelId=" +
baseReturns.getChannelId());
return;
}
// 3. 把响应放到对应的 Channel 的 map 中.
channel.putReturns(baseReturns);
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
21
22
23
24
25
26
27
28
29
30
31
32
33
34

3)实现channel.putReturns
把响应放到响应的hash 表中,同时唤醒等待响应的线程去消费.
public void putReturns (BaseReturns baseReturns) {
baseReturnsMap.put(baseReturns.getRid(), baseReturns);
synchronized (this) {
// 这⾥要唤醒所有等待的线程, 不能只唤醒⼀个.
notifyAll();
}
}1
2
3
4
5
6
7
关闭Connection
给Connection 实现close ⽅法
public void close() {
try {
callbackPool.shutdown();
channelMap = null;
inputStream.close();
outputStream.close();
socket.close();
} catch (IOException e) {
e.printStackTrace();
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
测试客⼾端-服务器创建MqClientTests
public class MqClientTests {
private BrokerServer brokerServer = null;
private Thread t = null;
private ConnectionFactory factory = null;1
2
3
4
5

@BeforeEach
public void setUp() throws IOException {
JavaMessageQueueApplication.ac =
SpringApplication.run(JavaMessageQueueApplication.class);
t = new Thread(() -> {
try {
brokerServer = new BrokerServer (9090);
brokerServer.start();
} catch (IOException e) {
e.printStackTrace();
}
});
t.start();
factory = new ConnectionFactory ();
factory.setHost( "127.0.0.1" );
factory.setPort( 9090);
}
@AfterEach
public void tearDown () throws IOException, InterruptedException {
// 结束服务器
brokerServer.stop();
// 等待线程结束
t.join();
// 关闭 Spring 服务器
JavaMessageQueueApplication.ac.close();
// 删除服务器的数据⽂件
File dbFile = new File("meta.db" );
dbFile.delete();
// 删除数据⽂件
File dataFile = new File("./data" );
FileUtils.deleteDirectory(dataFile);
factory = null;
}
}6
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
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
编写测试⽤例
@Test
public void testConnection () throws IOException {
Connection connection = factory.newConnection();
Assertions.assertNotNull(connection);1
2
3
4

}
@Test
public void testChannel () throws IOException {
Connection connection = factory.newConnection();
Assertions.assertNotNull(connection);
Channel channel = connection.createChannel();
Assertions.assertNotNull(channel);
}
@Test
public void testExchange () throws IOException, InterruptedException {
Connection connection = factory.newConnection();
Assertions.assertNotNull(connection);
Channel channel = connection.createChannel();
Assertions.assertNotNull(channel);
boolean ok = channel.exchangeDeclare( "testExchange" , ExchangeType.DIRECT,
true, false, null);
Assertions.assertTrue(ok);
ok = channel.exchangeDelete( "testExchange" );
Assertions.assertTrue(ok);
channel.close();
connection.close();
}
@Test
public void testQueue () throws IOException {
Connection connection = factory.newConnection();
Assertions.assertNotNull(connection);
Channel channel = connection.createChannel();
Assertions.assertNotNull(channel);
boolean ok = channel.queueDeclare( "testQueue" , true, false, false, null);
Assertions.assertTrue(ok);
ok = channel.queueDelete( "testQueue" );
Assertions.assertTrue(ok);
channel.close();
connection.close();
}
@Test
public void testBind () throws IOException {
Connection connection = factory.newConnection();
Assertions.assertNotNull(connection);5
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
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50

Channel channel = connection.createChannel();
Assertions.assertNotNull(channel);
boolean ok = channel.exchangeDeclare( "testExchange" , ExchangeType.DIRECT,
true, false, null);
Assertions.assertTrue(ok);
ok = channel.queueDeclare( "testQueue" , true, false, false, null);
Assertions.assertTrue(ok);
ok = channel.queueBind( "testQueue" , "testExchange" );
Assertions.assertTrue(ok);
ok = channel.queueUnbind( "testQueue" , "testExchange" );
Assertions.assertTrue(ok);
channel.close();
connection.close();
}
@Test
public void testMessageDirect () throws IOException, MqException,
InterruptedException {
Connection connection = factory.newConnection();
Assertions.assertNotNull(connection);
Channel channel = connection.createChannel();
Assertions.assertNotNull(channel);
boolean ok = channel.exchangeDeclare( "testExchange" , ExchangeType.DIRECT,
true, false, null);
Assertions.assertTrue(ok);
ok = channel.queueDeclare( "testQueue" , true, false, false, null);
Assertions.assertTrue(ok);
byte[] requestBody = "hello".getBytes();
// DIRECT 模式, routingKey 就是队列名字
// 发送的时候 basicProperties 可以是空着的. 服务器会进⾏构造. 订阅者收到的消息则是带有完整 basicProperties 的.
ok = channel.basicPublish( "testExchange" , "testQueue" , null, requestBody);
Assertions.assertTrue(ok);
ok = channel.basicConsume( "testQueue" , true, new Consumer () {
@Override
public void handleDelivery (String consumerTag, BasicProperties
properties, byte[] responseBody) {
System.out.println( "[消费数据] 开始!");
System.out.println( "consumerTag=" + consumerTag);
System.out.println( "properties=" + properties);51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92

String bodyString = new String(responseBody, 0,
responseBody.length);
System.out.println( "body=" + bodyString);
Assertions.assertEquals(requestBody, responseBody);
}
});
Assertions.assertTrue(ok);
// 等待数据消费完.
Thread.sleep( 500);
channel.close();
connection.close();
}
@Test
public void testMessageFanout () throws IOException, MqException,
InterruptedException {
Connection connection = factory.newConnection();
Assertions.assertNotNull(connection);
Channel channel1 = connection.createChannel();
Assertions.assertNotNull(channel1);
boolean ok = channel1.exchangeDeclare( "testExchange" , ExchangeType.FANOUT,
true, false, null);
Assertions.assertTrue(ok);
ok = channel1.queueDeclare( "testQueue1" , true, false, false, null);
Assertions.assertTrue(ok);
ok = channel1.queueDeclare( "testQueue2" , true, false, false, null);
Assertions.assertTrue(ok);
ok = channel1.queueBind( "testQueue1" , "testExchange" );
Assertions.assertTrue(ok);
ok = channel1.queueBind( "testQueue2" , "testExchange" );
Assertions.assertTrue(ok);
byte[] requestBody = "hello".getBytes();
// FANOUT 模式, routingKey 不需要
ok = channel1.basicPublish( "testExchange" , "", null, requestBody);
Assertions.assertTrue(ok);
ok = channel1.basicConsume( "testQueue1" , true, new Consumer () {
@Override
public void handleDelivery (String consumerTag, BasicProperties
properties, byte[] responseBody) throws MqException, IOException {
System.out.println( "consumerTag=" + consumerTag);
System.out.println( "properties=" + properties);93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134

String bodyString = new String(responseBody, 0,
responseBody.length);
System.out.println( "body=" + bodyString);
Assertions.assertEquals(requestBody, responseBody);
}
});
Assertions.assertTrue(ok);
Channel channel2 = connection.createChannel();
Assertions.assertNotNull(channel1);
ok = channel2.basicConsume( "testQueue2" , true, new Consumer () {
@Override
public void handleDelivery (String consumerTag, BasicProperties
properties, byte[] responseBody) throws MqException, IOException {
System.out.println( "consumerTag=" + consumerTag);
System.out.println( "properties=" + properties);
String bodyString = new String(responseBody, 0,
responseBody.length);
System.out.println( "body=" + bodyString);
Assertions.assertEquals(requestBody, responseBody);
}
});
Assertions.assertTrue(ok);
Thread.sleep( 1000);
channel1.close();
channel2.close();
connection.close();
}
@Test
public void testMessageTopic () throws IOException, MqException,
InterruptedException {
Connection connection = factory.newConnection();
Assertions.assertNotNull(connection);
Channel channel = connection.createChannel();
Assertions.assertNotNull(channel);
boolean ok = channel.exchangeDeclare( "testExchange" , ExchangeType.TOPIC,
true, false, null);
Assertions.assertTrue(ok);
ok = channel.queueDeclare( "testQueue" , true, false, false, null);
Assertions.assertTrue(ok);
ok = channel.queueBind( "testQueue" , "testExchange" , "aaa.#");135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176

byte[] requestBody = "hello".getBytes();
ok = channel.basicPublish( "testExchange" , "aaa.bbb.ccc" , null,
requestBody);
Assertions.assertTrue(ok);
ok = channel.basicConsume( "testQueue" , true, new Consumer () {
@Override
public void handleDelivery (String consumerTag, BasicProperties
properties, byte[] responseBody) {
System.out.println( "[消费数据] 开始!");
System.out.println( "consumerTag=" + consumerTag);
System.out.println( "properties=" + properties);
String bodyString = new String(responseBody, 0,
responseBody.length);
System.out.println( "body=" + bodyString);
Assertions.assertEquals(requestBody, responseBody);
}
});
Assertions.assertTrue(ok);
// 等待数据消费完.
Thread.sleep( 500);
channel.close();
connection.close();
}177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
⼗四.案例:基于MQ的⽣产者消费者模型
⽣产者:
public class DemoProducer {
public static void main(String[] args) throws IOException,
InterruptedException {
System.out.println( "启动⽣产者!");
ConnectionFactory factory = new ConnectionFactory ();
factory.setHost( "127.0.0.1" );
factory.setPort( 9090);
Connection connection = factory.newConnection();
Channel channel = connection.createChannel();1
2
3
4
5
6
7
8
9

channel.exchangeDeclare( "testExchange" , ExchangeType.DIRECT, true,
false, null);
channel.queueDeclare( "testQueue" , true, false, false, null);
byte[] body = "hello".getBytes();
boolean ok = channel.basicPublish( "testExchange" , "testQueue" , null,
body);
System.out.println( "投递消息完成! ok=" + ok);
Thread.sleep( 500);
channel.close();
connection.close();
}
}10
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
21
消费者:
public class DemoConsumer {
public static void main(String[] args) throws IOException, MqException,
InterruptedException {
System.out.println( "启动消费者!");
ConnectionFactory factory = new ConnectionFactory ();
factory.setHost( "127.0.0.1" );
factory.setPort( 9090);
Connection connection = factory.newConnection();
Channel channel = connection.createChannel();
channel.exchangeDeclare( "testExchange" , ExchangeType.DIRECT, true,
false, null);
channel.queueDeclare( "testQueue" , true, false, false, null);
channel.basicConsume( "testQueue" , true, new Consumer () {
@Override
public void handleDelivery (String consumerTag, BasicProperties
properties, byte[] body) {
System.out.println( "[消费数据] 开始!");
System.out.println( "consumerTag=" + consumerTag);
System.out.println( "properties=" + properties);
String bodyString = new String(body, 0, body.length);
System.out.println( "body=" + bodyString);
System.out.println( "[消费数据] 完毕!");
}
});1
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
21
22
23
24

while (true) {
Thread.sleep( 500);
}
}
}25
26
27
28
29
⼗五.扩展功能
•虚拟主机管理
•⽤⼾管理/⽤⼾认证
•交换机/队列的独占模式和⾃动删除.
•发送⽅确认(broker 给⽣产者的确认应答)
•拒绝应答(nack)
•死信队列
•管理接⼝
•管理⻚⾯