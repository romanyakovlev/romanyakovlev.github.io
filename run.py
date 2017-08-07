from jinja2 import Environment, FileSystemLoader
import markdown
import json
import os


def make_environment(root_folder_path):
  loader = FileSystemLoader(root_folder_path)
  template_environment = Environment(loader=loader)
  return template_environment


def render_static_to_html(template_environment, root_folder_path):
  path_to_static = os.path.join(root_folder_path, 'static.html')
  relative_path_static = os.path.join('templates', 'static_template.html')
  static_template = template_environment.get_template(relative_path_static)
  static_template.stream(path_to_dir= ' ').dump(path_to_static)


def get_rendered_markdown_text_from_file(path_to_file):
  markdown_text = open(path_to_file).read()
  md = markdown.Markdown(extensions = ['markdown.extensions.meta'])
  rendered_text = md.convert(markdown_text)
  return rendered_text


def create_folder_for_topic_if_it_does_not(file_name_with_html_format):
  only_folders_path = os.path.split(file_name_with_html_format)[0]
  if not os.path.exists(only_folders_path):
    os.makedirs(only_folders_path)


def create_full_file_path(article_path, root_folder_path):
  file_name_without_md_format = os.path.splitext(article_path)[0]
  file_name_with_html_format = '.'.join([file_name_without_md_format, 'html'])
  full_path = os.path.join(root_folder_path, 'articles', '.'.join([file_name_with_html_format.split('/')[-1].split('.')[0], 'html']))
  return full_path


def create_relative_file_path(article_path):
  file_name_without_md_format = os.path.splitext(article_path)[0]
  file_name_with_html_format = '.'.join([file_name_without_md_format, 'html'])
  relative_path = os.path.join('articles', '.'.join([file_name_with_html_format.split('/')[-1].split('.')[0], 'html']))
  return relative_path


def create_file(file_path):
  open(file_path, 'w').close()


def get_title_from_markdown(mk_name):
    markdown_text = open('articles_md_templtate/'+mk_name.split('.')[0]+'.md').read()
    md = markdown.Markdown(extensions = ['markdown.extensions.meta'])
    rendered_text = md.convert(markdown_text)
    return md.Meta


def render_markdown_to_html(template_environment, article_dict, root_folder_path, index_link):
  relative_path_markdown = os.path.join('templates', 'md_template.html')
  markdown_template = template_environment.get_template(relative_path_markdown)
  article_path = article_dict.split('/')[-1]
  path_to_markdown = os.path.join('articles_md_templtate', article_path)
  html_text = get_rendered_markdown_text_from_file(path_to_markdown)
  full_file_path = create_full_file_path(article_path, root_folder_path)
  create_file(full_file_path)
  markdown_template.stream(html_text=html_text, article=get_title_from_markdown(article_path), index_link=index_link).dump(full_file_path)


def render_all_markdowns_to_html(template_environment, root_folder_path, index_link):
  for x, y, z in os.walk(os.getcwd()+'/articles_md_templtate/'):
      for article in z:
          article_path = os.path.join(x, article)
          render_markdown_to_html(template_environment, article_path, root_folder_path, index_link)


def render_index_to_html(template_environment, root_folder_path, index_link):
  path_to_index = 'index.html'
  relative_path_index = os.path.join('templates', 'index_template.html')
  static_template = template_environment.get_template(relative_path_index)
  articles_arr = []
  for x, y, z in os.walk(os.getcwd()+'/articles_md_templtate/'):
      for article in z:
          article_dict = {}
          article_dict['href'] = '.'.join([*article.split('.')[:-1], 'html'])
          article_dict['title'] = get_title_from_markdown(article_dict['href'])
          articles_arr.append(article_dict)
  static_template.stream(articles_arr=articles_arr, index_link=index_link).dump(path_to_index)


def make_all_data():
  root_folder_path = os.getcwd()
  template_environment = make_environment(root_folder_path)
  index_link = os.path.join(os.sep, 'index.html')
  return root_folder_path, template_environment, index_link


def render_templates(template_environment, root_folder_path, index_link):
  render_static_to_html(template_environment, root_folder_path)
  render_all_markdowns_to_html(template_environment, root_folder_path, index_link)
  render_index_to_html(template_environment, root_folder_path, index_link)


if __name__ == '__main__':
  root_folder_path, template_environment, index_link = make_all_data()
  render_templates(template_environment, root_folder_path, index_link)
