drop table log;


create table log
	(
		log_reqstart timestamp,
		log_reqtime number(12,6),
		log_instance varchar2(256),
		log_host varchar2(64),
		log_useragent varchar2(4000),
		log_url varchar2(4000),
		log_method varchar2(64),
		log_status integer,
		log_bytesin integer,
		log_bytesout integer,
		log_bytesbodyout integer,
		log_encoding varchar2(64),
		log_mimetype varchar2(64),
		log_charset varchar2(64),
		log_referer varchar2(4000),
		log_session varchar2(256),
		log_coid integer
	);


create or replace procedure log_insert
	(
		p_log_reqstart in timestamp := null,
		p_log_reqtime in number := null,
		p_log_instance in varchar2 := null,
		p_log_host in varchar2 := null,
		p_log_useragent in varchar2 := null,
		p_log_url in varchar2 := null,
		p_log_method in varchar2 := null,
		p_log_status in integer := null,
		p_log_bytesin in integer := null,
		p_log_bytesout in integer := null,
		p_log_bytesbodyout in integer := null,
		p_log_encoding in varchar2 := null,
		p_log_mimetype in varchar2 := null,
		p_log_charset in varchar2 := null,
		p_log_referer in varchar2 := null,
		p_log_session in varchar2 := null,
		p_log_coid in integer := null
	)
	as
		pragma autonomous_transaction;
	begin
		insert into log
		(
			log_reqstart,
			log_reqtime,
			log_instance,
			log_host,
			log_useragent,
			log_url,
			log_method,
			log_status,
			log_bytesin,
			log_bytesout,
			log_bytesbodyout,
			log_encoding,
			log_mimetype,
			log_charset,
			log_referer,
			log_session,
			log_coid
		)
		values
		(
			p_log_reqstart,
			p_log_reqtime,
			p_log_instance,
			p_log_host,
			p_log_useragent,
			p_log_url,
			p_log_method,
			p_log_status,
			p_log_bytesin,
			p_log_bytesout,
			p_log_bytesbodyout,
			p_log_encoding,
			p_log_mimetype,
			p_log_charset,
			p_log_referer,
			p_log_session,
			p_log_coid
		);
		commit;
	end;
/
